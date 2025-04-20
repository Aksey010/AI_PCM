import streamlit as st

st.subheader('Группы компонентов')

def info():
    with st.container(border=True):

        st.subheader('Полипропилены')
        with st.container(border=True):
            st.markdown('##### Полипропилены группы SPP1')
            with st.container(border=True):
                st.write('- Блок-сополимер пропилена с этиленом PP I120 GP/5')
                st.write('- Блок-сополимер пропилена с этиленом PP I120 GP/3')
            st.markdown('##### Полипропилены группы SPP2')
            with st.container(border=True):
                st.write('- Блок-сополимер пропилена с этиленом PP I013 GP/5')
            st.markdown('##### Полипропилены группы SPP3')
            with st.container(border=True):
                st.write('- Блок-сополимер пропилена с этиленом SIBEX PP T192 IM/5')
            st.markdown('##### Полипропилены группы SPP4')
            with st.container(border=True):
                st.write('- Блок-сополимер пропилена с этиленом SIBEX PP T122 IM/5')
            st.markdown('##### Полипропилены группы SPP5')
            with st.container(border=True):
                st.write('- Блок-сополимер пропилена с этиленом SIBEX PP T172 IM/5')
            st.markdown('##### Полипропилены группы SPP6')
            with st.container(border=True):
                st.write('- Блок-сополимер пропилена с этиленом SIBEX PP I452 IM/5')
            st.markdown('##### Полипропилены группы SPP7')
            with st.container(border=True):
                st.write('- Блок-сополимер пропилена с этиленом SIBEX PP I602 IM/5')
            st.markdown('##### Полипропилены группы SPP8')
            with st.container(border=True):
                st.write('- Блок-сополимер пропилена с этиленом SIBEX PP T082 IM/5')
            st.markdown('##### Полипропилены группы GPP1')
            with st.container(border=True):
                st.write('- Гомополимер пропилена РР Н120 GP/3')
                st.write('- Гомополимер пропилена Бален 01130')
            st.markdown('##### Полипропилены группы GPP2')
            with st.container(border=True):
                st.write('- Гомополимер пропилена РР Н030 GP/3')
                st.write('- Гомополимер пропилена Бален 01030')
            st.markdown('##### Полипропилены группы GPP3')
            with st.container(border=True):
                st.write('- Гомополимер пропилена РР Н250 GР/3 ')
            st.markdown('##### Полипропилены группы GPP4')
            with st.container(border=True):
                st.write('- Гомополимер пропилена РР Н450 GP/3')

        st.subheader('Модификаторы')
        with st.container(border=True):
            st.markdown('##### Модификаторы группы MP1')
            with st.container(border=True):
                st.write('- Модификатор Hifax X 1956 A')
            st.markdown('##### Модификаторы группы MP2')
            with st.container(border=True):
                st.write('- Модификатор PP 01-ATS')
                st.write('- Модификатор PP M017 AS')
            st.markdown('##### Модификаторы группы MUV1')
            with st.container(border=True):
                st.write('- Полиолефиновый эластомер Lucene LС 168')
            st.markdown('##### Модификаторы группы MUV2')
            with st.container(border=True):
                st.write('- Полиолефиновый эластомер Lucene LС 170')
                st.write('- Полиолефиновый эластомер Solumer 871')
                st.write('- Полиолефиновый эластомер FORTIFY C1070D')
            st.markdown('##### Модификаторы группы MUV3')
            with st.container(border=True):
                st.write('- Полиолефиновый эластомер Lucene LС 670')
                st.write('- Полиолефиновый эластомер Solumer 875')
            st.markdown('##### Модификаторы группы MC1')
            with st.container(border=True):
                st.write('- Эпоксидная смола марка Olin SOLID EPOXY RESIN')

        st.subheader('Наполнители')
        with st.container(border=True):
            st.markdown('##### Наполнители группы N1')
            with st.container(border=True):
                st.write('- Тальк HTP05L')
                st.write('- Тальк Luzenac A-7C')
                st.write('- Тальк MinTalc 98-05C')
                st.write('- Тальк MinTalc 97-05C')
                st.write('- Тальк Steamic T1CA')
            st.markdown('##### Наполнители группы N2')
            with st.container(border=True):
                st.write('- Тальк RoseTalc RT-ST 20')
                st.write('- Тальк LUZENAC E15')
            st.markdown('##### Наполнители группы N3')
            with st.container(border=True):
                st.write('- Тальк RoseTalc GС 20EX')
            st.markdown('##### Наполнители группы N4')
            with st.container(border=True):
                st.write('- Тальк KKT Type B')
                st.write('- Тальк KKT Type A')
                st.write('- Тальк Luzenac 20M0')
                st.write('- Тальк RoseTalc RT-ST 30')
            st.markdown('##### Наполнители группы N5')
            with st.container(border=True):
                st.write('- Карбонат кальция Omyacarb 2UR')

        st.subheader('Стабилизаторы')
        with st.container(border=True):
            st.markdown('##### Стабилизаторы группы TS1')
            with st.container(border=True):
                st.write('- Термостабилизатор Ирганокс (IRGANOX) 1010 FF')
                st.write('- Термостабилизатор Ирганокс (IRGANOX) PS 802 FL')
                st.write('- Термостабилизатор Иргафос (IRGAFOS) 168 FF')
                st.write('- DSTDP')
            st.markdown('##### Стабилизаторы группы SS1')
            with st.container(border=True):
                st.write('- Светостабилизатор Тинувин (TINUVIN) 791 FB')
                st.write('- Светостабилизатор Химассорб (Chimassorb) 81 FL')
                st.write('- Светостабилизатор Addworks ATR 945 MP')
                st.write('- Светостабилизатор Cyasorb Cyxtra V9900')
                st.write('- Светостабилизатор Cynergy B877')
                st.write('- Светостабилизатор UV-5411')

        st.subheader('Смазки')
        with st.container(border=True):
            st.markdown('##### Смазки группы S1')
            with st.container(border=True):
                st.write('- Силиконовый концентрат Multibase MB 50-001G2')
            st.markdown('##### Смазки группы S2')
            with st.container(border=True):
                st.write('- Эрукамид Финавакс Е (Finawax E)')
            st.markdown('##### Смазки группы S3')
            with st.container(border=True):
                st.write('- Олеамид Финавакс О (Finawax O)')
            st.markdown('##### Смазки группы S4')
            with st.container(border=True):
                st.write('- Стеарат кальция CEASIT POE')
                st.write('- Стеарат кальция Ligastar CA 350')

        st.subheader('Красители')
        with st.container(border=True):
            st.markdown('##### Красители группы K1')
            with st.container(border=True):
                st.write('- Концентрат красителя Томполен 158-30 КТУ П-245')
                st.write('- Концентрат красителя КТУ ПЭ 30')
                st.write('- Концентрат красителя КТУ ПЭ 50')
                st.write('- Концентрат красителя HAIER РР-2')
                st.write('- Концентрат красителя PP-4 alliance black AS6')
                st.write('- Концентрат красителя СК Black 190826-HP черный (Ампасет) Черный концентрат')
                st.write('- Концентрат красителя 805-РР-5')
                st.write('- Концентрат красителя 897-РР-2 (РР 21Т-IM антрацит)')

if st.session_state.logged_in == True:
    info()
else:
    st.warning('Требуется предварительная авторизация!')