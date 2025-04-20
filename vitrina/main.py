import streamlit as st
st.set_page_config(layout="wide")

st.markdown('#### Автоматизированная информационная система подбора компаунда')

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    with st.form("my_form"):
        st.markdown("**Авторизация:**")
        login_val = st.text_input("Логин:")
        password_val = st.text_input("Пароль:", type='password')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Войти")
        if submitted:
            if login_val=='admin' and password_val=='asd234':
                st.session_state.logged_in = True
                st.rerun()
            else: st.error('Логин и/или пароль указаны не верно! Попробуйте повторить ввод.')


def logout():
    if st.button("Выйти"):
        st.session_state.logged_in = False
        st.rerun()

with st.sidebar:
    st.markdown('**Автоматизированная информационная система подбора компаунда (АИС ПК)**')
    st.image('logo_uii_thp.png')
login_page = st.Page(login, title="Войти", icon=":material/login:")
logout_page = st.Page(logout, title="Выйти", icon=":material/logout:")


haract_page2 = st.Page("pfh2.py", title="по характеристикам", icon=":material/keyboard_double_arrow_right:")
#sostav_page = st.Page("pfs.py", title="по составу", icon=":material/keyboard_double_arrow_right:")
komponents_info = st.Page("komponents_info.py", title="Справочник компонентов", icon=":material/keyboard_double_arrow_right:")


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Прогнозирование": [haract_page2, komponents_info],
            "Аккаунт": [logout_page]

        }
    )

else:
    pg = st.navigation([login_page])

pg.run()

