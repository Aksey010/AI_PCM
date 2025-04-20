import tensorflow as tf
from tensorflow.keras import layers
from keras_tuner import HyperModel

class ExpandDimsLayer(layers.Layer):
    def __init__(self, axis, **kwargs):
        super(ExpandDimsLayer, self).__init__(**kwargs)
        self.axis = axis

    def call(self, inputs):
        return tf.expand_dims(inputs, axis=self.axis)

class HybridKANTransformerBlock(layers.Layer):
    def __init__(self, num_heads, key_dim, ff_dim, output_dim, **kwargs):
        super(HybridKANTransformerBlock, self).__init__(**kwargs)
        self.attention = layers.MultiHeadAttention(num_heads=num_heads, key_dim=key_dim)
        self.ffn = tf.keras.Sequential([
            layers.Dense(ff_dim, activation="relu"),
            layers.Dense(key_dim),
        ])
        self.output_projection = layers.Dense(output_dim)
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = layers.Dropout(0.1)
        self.dropout2 = layers.Dropout(0.1)

    def call(self, inputs, training=False):
        attn_output = self.attention(inputs, inputs, training=training)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1, training=training)
        ffn_output = self.dropout2(ffn_output, training=training)
        if ffn_output.shape[-1] != out1.shape[-1]:
            ffn_output = self.output_projection(ffn_output)
        return self.layernorm2(out1 + ffn_output)

class HybridKANTransformerModel(HyperModel):
    def build(self, hp):
        inputs = tf.keras.Input(shape=(35,))  # Изменение размера входных данных

        kan_layer = layers.Dense(hp.Int('units_kan', min_value=32, max_value=256, step=32), activation='relu')(inputs)
        kan_layer = ExpandDimsLayer(axis=1)(kan_layer)  # Добавление оси для совместимости с Transformer
        transformer_block = HybridKANTransformerBlock(
            num_heads=hp.Int('num_heads', min_value=2, max_value=8, step=2),
            key_dim=hp.Int('key_dim', min_value=32, max_value=128, step=32),
            ff_dim=hp.Int('ff_dim', min_value=32, max_value=256, step=32),
            output_dim=kan_layer.shape[-1]
        )
        x = transformer_block(kan_layer, training=True)
        x = layers.GlobalAveragePooling1D()(x)
        x = layers.Dropout(0.1)(x)
        x = layers.Dense(hp.Int('units_dense', min_value=32, max_value=256, step=32), activation='relu')(x)
        outputs = layers.Dense(77, activation='linear')(x)  # Изменение размерности выходных данных

        model = tf.keras.Model(inputs=inputs, outputs=outputs)
        model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        return model
