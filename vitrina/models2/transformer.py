import torch
import torch.nn as nn
import torch.optim as optim

# Определение модели трансформера
class TransformerModel(nn.Module):
    def __init__(self, d_model=36, output_dim=30, nhead=3, num_encoder_layers=3, dim_feedforward=512, dropout=0.1):
        super(TransformerModel, self).__init__()
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, batch_first=True, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout)
        self.transformer_encoder = nn.TransformerEncoder(self.encoder_layer, num_layers=num_encoder_layers, enable_nested_tensor=False)
        self.fc_out = nn.Linear(d_model, output_dim)

    def forward(self, src):
        src = src.unsqueeze(1)  # Добавление batch dimension
        transformer_output = self.transformer_encoder(src)
        output = self.fc_out(transformer_output.squeeze(1))  # Удаление batch dimension
        return output