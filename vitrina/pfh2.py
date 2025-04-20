import streamlit as st
import pandas as pd
import models2.pred2 as pred2
import io

buffer = io.BytesIO()

st.markdown('**Прогнозирование по характеристикам**')

#st.page_link("pfh.py", label="Предыдущая версия", icon=":material/keyboard_double_arrow_right:")

def predict_form():
    with st.form("my_form"):
        with st.container(border=True):
            h1 = st.number_input('Показатель текучести расплава, 230°С/2,16 кгс, гр/10 мин (Y1)', 0.0, value=10.2)
            h2 = st.number_input('Зольность, % (Y2)', 0.0, value=15.0)
            h3 = st.number_input('Плотность, г/см3 (Y3)', 0.0, value=1.0)
        with st.container(border=True):
            st.write('Растяжение:')
            h4 = st.number_input('Предел текучести при растяжении, МПа (Y4)', 0.0, value=23.5)
            h17 = st.number_input('Прочность при растяжении, МПа (Y17)', 0.0, value=0.0)
            h6 = st.number_input('Относительное удлинение при пределе текучести, % (Y6)', 0.0, value=0.0)
            h5 = st.number_input('Относительное удлинение при разрыве, % (Y5)', 0.0, value=0.0)
            h15 = st.number_input('Модуль упругости при растяжении, МПа (Y15)', 0.0, value=0.0)
        with st.container(border=True):
            st.write('Изгиб:')
            h14 = st.number_input('Модуль упругости при изгибе, МПа (Y14)', 0.0, value=1953.0)
            h16 = st.number_input('Изгибающее напряжение при максимальной нагрузке, МПа (Y16)', 0.0, value=0.0)

        with st.container(border=True):
            st.write('Удар:')
            col2_1, col2_2 = st.columns(2)
            with col2_1:
                st.write('Ударная вязкость по Изоду на образцах с надрезом (кДж/м2):')
                h10 = st.number_input('+23°С (Y10)', 0.0, value=7.9)
                h11 = st.number_input('-23°С (Y11)', 0.0, value=0.0)
                h12 = st.number_input('-30°С (Y12)', 0.0, value=3.3)
                h13 = st.number_input('без надреза -30°С (Y13)', 0.0, value=0.0)

            with col2_2:
                st.write('Ударная вязкость по Шарпи на образцах с надрезом (кДж/м2):')
                h7 = st.number_input('в ребро, +23°С (Y7)', 0.0, value=0.0)
                h8 = st.number_input('плашмя, +23°С (Y8)', 0.0, value=0.0)
                h9 = st.number_input('в ребро, -40°С (Y9)', 0.0, value=0.0)

        with st.container(border=True):
            st.write('Тепловые характеристики:')
            col3_1, col3_2 = st.columns(2)
            with col3_1:
                st.write('Темпертура изгиба под нагрузкой (°С):')
                h20 = st.number_input('0,45 МПа (Y20)', 0.0, value=0.0)
                h21 = st.number_input('0,45 МПа, (предварительный отжиг 90°С/30 мин) (Y21)', 0.0, value=0.0)
                h18 = st.number_input('1,8 МПа (Y18)', 0.0, value=0.0)
                h19 = st.number_input('1,8 МПа, (предварительный отжиг 90°С/30 мин) (Y19)', 0.0, value=0.0)

            with col3_2:
                st.write('Температура размягчения по Вика (°С):')
                h22 = st.number_input('при  нагрузке 10Н, 120°С/ч (Y22)', 0.0, value=0.0)
                h23 = st.number_input('при  нагрузке 50Н, 120°С/ч (Y23)', 0.0, value=0.0)

        with st.container(border=True):
            st.write('Усадка на образце 60х60х2 мм (%):')
            col4_1, col4_2, col4_3 = st.columns(3)
            with col4_1:
                st.write('Продольная:')
                h26 = st.number_input('50 МПа (Y26)', 0.0, value=0.0, key='h26')
                h27 = st.number_input('60 МПа (Y27)', 0.0, value=0.93, key='h27')
            with col4_2:
                st.write('Поперечная:')
                h28 = st.number_input('50 МПа (Y28)', 0.0, value=0.0, key='h28')
                h29 = st.number_input('60 МПа (Y29)', 0.0, value=0.96, key='h29')
            with col4_3:
                st.write('Средняя:')
                h24 = st.number_input('50 МПа (Y24)', 0.0, value=0.0)
                h25 = st.number_input('60 МПа (Y25)', 0.0, value=0.0)

        with st.container(border=True):
            st.write('Стойкость к царапанью при нагрузке (dL):')
            col5_1, col5_2, col5_3 = st.columns(3)
            with col5_1:
                h30 = st.number_input('7Н на текстуре 203.30 (Y30)', 0.0, value=0.0)
                h32 = st.number_input('7Н на текстуре 213.26 (Y32)', 0.0, value=0.0)

            with col5_2:
                h31 = st.number_input('10Н на текстуре 203.30 (Y31)', 0.0, value=0.0)
                h33 = st.number_input('10Н на текстуре 213.26 (Y33)', 0.0, value=0.0)

            with col5_3:
                h34 = st.number_input('13Н на текстуре 203.30 (Y34)', 0.0, value=0.0)
                h35 = st.number_input('13Н на текстуре 213.26 (Y35)', 0.0, value=0.0)

        h36 = st.number_input('Внешний вид "тигровые полосы", балл (от 1 до 5, где 1 - NOK, 5 - OK) (Y36)', 0.0,
                              value=0.0)

        submitted = st.form_submit_button("Прогноз")
        if submitted:
            x = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22,
                 h23, h24, h25, h26, h27, h28, h29, h30, h31, h32, h33, h34, h35, h36]

            preds_min, preds = pred2.pred(x)
            zapros_titles = [
                'Показатель текучести расплава, 230°С/2,16 кгс, гр/10 мин (Y1)',
                'Зольность, % (Y2)',
                'Плотность, г/см3 (Y3)',
                'Предел текучести при растяжении, МПа (Y4)',
                'Прочность при растяжении, МПа (Y17)',
                'Относительное удлинение при пределе текучести, % (Y6)',
                'Относительное удлинение при разрыве, % (Y5)',
                'Модуль упругости при растяжении, МПа (Y15)',
                'Модуль упругости при изгибе, МПа (Y14)',
                'Изгибающее напряжение при максимальной нагрузке, МПа (Y16)',
                'Ударная вязкость по Изоду на образцах с надрезом (кДж/м2) +23°С (Y10)',
                'Ударная вязкость по Изоду на образцах с надрезом (кДж/м2) -23°С (Y11)',
                'Ударная вязкость по Изоду на образцах с надрезом (кДж/м2) -30°С (Y12)',
                'Ударная вязкость по Изоду на образцах с надрезом (кДж/м2) без надреза -30°С (Y13)',
                'Ударная вязкость по Шарпи на образцах с надрезом (кДж/м2) в ребро, +23°С (Y7)',
                'Ударная вязкость по Шарпи на образцах с надрезом (кДж/м2) плашмя, +23°С (Y8)',
                'Ударная вязкость по Шарпи на образцах с надрезом (кДж/м2) в ребро, -40°С (Y9)',
                'Темпертура изгиба под нагрузкой (°С) 0,45 МПа (Y20)',
                'Темпертура изгиба под нагрузкой (°С) (предварительный отжиг 90°С/30 мин), 0,45 МПа (Y21)',
                'Темпертура изгиба под нагрузкой (°С) 1,8 МПа (Y18)',
                'Темпертура изгиба под нагрузкой (°С) (предварительный отжиг 90°С/30 мин), 1,8 МПа (Y19)',
                'Температура размягчения по Вика (°С) при  нагрузке 10Н, 120°С/ч (Y22)',
                'Температура размягчения по Вика (°С) при  нагрузке 50Н, 120°С/ч (Y23)',
                'Усадка на образце 60х60х2 мм (%) Продольная 50 МПа (Y26)',
                'Усадка на образце 60х60х2 мм (%) Продольная 60 МПа (Y27)',
                'Усадка на образце 60х60х2 мм (%) Поперечная 50 МПа (Y28)',
                'Усадка на образце 60х60х2 мм (%) Поперечная 60 МПа (Y29)',
                'Усадка на образце 60х60х2 мм (%) Средняя 50 МПа (Y24)',
                'Усадка на образце 60х60х2 мм (%) Средняя 60 МПа (Y25)',
                'Стойкость к царапанью при нагрузке (dL) 7Н на текстуре 203.30 (Y30)',
                'Стойкость к царапанью при нагрузке (dL) 7Н на текстуре 203.30 (Y32)',
                'Стойкость к царапанью при нагрузке (dL) 10Н на текстуре 203.30 (Y31)',
                'Стойкость к царапанью при нагрузке (dL) 10Н на текстуре 213.26 (Y33)',
                'Стойкость к царапанью при нагрузке (dL) 13Н на текстуре 203.30 (Y34)',
                'Стойкость к царапанью при нагрузке (dL) 13Н на текстуре 213.26 (Y35)',
                'Внешний вид "тигровые полосы", балл (от 1 до 5, где 1 - NOK, 5 - OK) (Y36)'
            ]
            zapros_data=[h1,h2,h3, h4, h17, h6, h5, h15, h14, h16, h10, h11, h12, h13, h7, h8, h9,
                         h20,h21,h18,h19, h22,h23,h26,h27,h28,h29,h24,h25,h30,h32,h31,h33,h34,h35,h36]
            zapros = {'titles': zapros_titles, 'data': zapros_data}
            zapros = pd.DataFrame(zapros)
            preds = pd.DataFrame(preds)
            preds_min = pd.DataFrame(preds_min)
            with st.container(border=True):
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    zapros.to_excel(writer, sheet_name='Запрос')
                    preds_min.to_excel(writer, sheet_name='Состав')

            with st.container(border=True):
                st.markdown('**Состав:**')
                st.dataframe(preds_min, width=1500, use_container_width=True)


    st.download_button(
        label="Скачать в Excel",
        data=buffer,
        file_name="compaund.xlsx",
        mime="application/vnd.ms-excel"
    )


if st.session_state.logged_in == True:
    predict_form()
else:
    st.warning('Требуется предварительная авторизация!')