import numpy as np
import keras
import tensorflow as tf
import joblib
import models2.transformer as transformer
import models2.hybrid as hybrid
import torch

titles=[
    "Полипропилен SPP1 (PP I120 GP/5)",
    "Полипропилен SPP2 (PP I013 GP/5)",
    "Полипропилен SPP3 (PP T192 IM/5)",
    "Полипропилен SPP4 (PP T122 IM/5)",
    "Полипропилен SPP5 (PP T172 IM/5)",
    "Полипропилен SPP6 (PP I452 IM/5)",
    "Полипропилен SPP7 (PP I602 IM/5)",
    "Полипропилен SPP8 (PP T082 IM/5)",
    "Полипропилен GPP1 (РР Н120 GP/3)",
    "Полипропилен GPP2 (РР Н030 GP/3)",
    "Полипропилен GPP3 (РР Н250 GР/3)",
    "Полипропилен GPP4 (РР Н450 GP/3)",
    "Модификатор MP1 (Hifax X 1956 A)",
    "Модификатор MP2 (PP 01-ATS)",
    "Модификатор MUV1 (LС 168)",
    "Модификатор MUV2 (LС 170)",
    "Модификатор MUV3 (LС 670)",
    "Модификатор MC1 (Olin SOLID EPOXY RESIN)",
    "Наполнитель N1 (HTP05L)",
    "Наполнитель N2 (RT-ST 20)",
    "Наполнитель N3 (RoseTalc GС 20EX)",
    "Наполнитель N4 (KKT Type B)",
    "Наполнитель N5 (Omyacarb 2UR)",
    "Стабилизатор TS1 (IRGANOX 1010 FF)",
    "Стабилизатор SS1 (TINUVIN 791 FB)",
    "Смазка S1 (MB 50-001G2)",
    "Смазка S2 (Finawax E)",
    "Смазка S3 (Finawax O)",
    "Смазка S4 (CEASIT POE)",
    "Краситель K1 (Томполен 158-30 КТУ П-245)"
]

def pred(y):
    predicts = []
    for id in range(1,5):
        if id==1 or id==4:
            model=keras.models.load_model(f'models2/{id}/model.keras')
        elif id==2:
            model = transformer.TransformerModel()
            model.load_state_dict(torch.load(f'models2/{id}/model.zip'))
            model.eval()
        elif id==3:
            custom_objects = {
                'ExpandDimsLayer': hybrid.ExpandDimsLayer,
                'HybridKANTransformerBlock': hybrid.HybridKANTransformerBlock,
            }
            model = tf.keras.models.load_model(f'models2/{id}/model.keras', custom_objects=custom_objects)

        scaler_x=joblib.load(f'models2/{id}/scaler_y.scl')
        scaler_y=joblib.load(f'models2/{id}/scaler_x.scl')
        y_query=np.array(y).reshape(-1,len(y))
        y_scal=scaler_y.transform(y_query)
        if id==1 or id==3: p=model.predict(y_scal)[0]
        elif id==2:
            with torch.no_grad():
                y_tensor=torch.tensor(y_scal, dtype=torch.float32)
                p=model(y_tensor)[0]
        elif id==4:
            classifier_pred, regressor_pred = model.predict(y_scal)
            classifier_pred_class = (classifier_pred > 0.3).astype(int)
            p = classifier_pred_class * regressor_pred
            p=p[0]

        p=p.reshape(1, len(p))
        pred_x=scaler_x.inverse_transform(p)
        #pred_x[pred_x<0]=0
        pr=[]
        for i in range(p.shape[1]):
            if pred_x[0][i]<0.1: val=0.0
            else: val=pred_x[0][i]
            pr.append(round(val,1))
        summa=sum(pr)
        for n in range(len(pr)):
            pr[n]=round(pr[n]*100/summa,1)
        razn=(sum(pr)-100)
        maximum_val=max(pr)
        maximum_index=pr.index(maximum_val)
        pr[maximum_index]=pr[maximum_index]-razn
        pr[maximum_index]=round(pr[maximum_index],1)
        predicts.append(pr)
    x_id=[]
    for i in range(p.shape[1]):
        x_id.append(f'X{i+1}')
    result={'X':x_id, 'title':titles, 'AutoML':predicts[0]}

    x_id_min = []
    titles_min = []
    m_0 = []
    m_1 = []
    m_2 = []
    m_3 = []
    for i in range(p.shape[1]):
        if round(predicts[0][i], 1) > 0 or round(predicts[1][i], 1) > 0 or round(predicts[2][i], 1) > 0 or round(predicts[3][i], 1) > 0:
            x_id_min.append(f'X{i + 1}')
            titles_min.append(titles[i])
            m_0.append(round(predicts[0][i], 1))
            m_1.append(round(predicts[1][i], 1))
            m_2.append(round(predicts[2][i], 1))
            m_3.append(round(predicts[3][i], 1))

    result_min = {'X': x_id_min, 'title': titles_min, 'AutoML': m_0, 'Transformer': m_1, 'Hybrid':m_2, '2_Regression':m_3}
    return result_min, result

