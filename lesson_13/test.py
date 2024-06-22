import streamlit as st

# Callback 函數
def cal_callback(col3):
    weight = st.session_state.weight_input_2
    height = st.session_state.height_input_2
    if weight <= 0 or height <= 0:
        col3.markdown("<br><br>", unsafe_allow_html=True)
        col3.error("輸入值不可為負值或零，請重新輸入。")
    else:
        bmi = weight / ((height / 100) ** 2)
        if bmi < 18.5:
            txt = "<font color=DarkBlue>**體重過輕**</font>"
        elif bmi < 24:
            txt = "<font color=green>**正常範圍**</font>"
        elif bmi < 27:
            txt = "<font color=red>**過重**</font>"
        elif bmi < 30:
            txt = "<font color=Fuchsia>**輕度肥胖**</font>"
        elif bmi < 35:
            txt = "<font color=DarkSalmon>**中度肥胖**</font>"
        else:
            txt = "<font color=BlueViolet>**重度肥胖**</font>"

        col3.markdown("<br><br>", unsafe_allow_html=True)
        col3.markdown(f"您的BMI值為: {bmi:.2f} <br> 體重: {txt}", unsafe_allow_html=True)

def clear_callback(col3):
    st.session_state.weight_input_2 = 0.0
    st.session_state.height_input_2 = 0.0
    #st.experimental_rerun()

def BMI_info():
    st.markdown('''
    |  | 身體質量指數(BMI)(kg/m²) | 腰圍(cm)  |
    |-|-|-|
    | 體重過輕 | BMI ＜ 18.5 | -  |
    | 正常範圍 | 18.5 ≦ BMI ＜ 24 | -  |
    | 異常範圍 | 過重：24 ≦ BMI ＜ 27 <br>輕度肥胖：27 ≦ BMI ＜ 30 <br>中度肥胖：30 ≦ BMI ＜ 35 <br>重度肥胖：BMI ≧ 35 | 男性：≧90公分  <br>女性：≧80公分  |
    ''', unsafe_allow_html=True)

# 自訂函式來顯示表單並處理輸入
def display_bmi_form(form_key, weight_key, height_key, session_flag=True):
    # 初始化
    if weight_key not in st.session_state:
        st.session_state[weight_key] = 0.0
    if height_key not in st.session_state:
        st.session_state[height_key] = 0.0

    with st.form(form_key):
        st.markdown(f'<h3 style="color:purple;text-align:center">BMI值計算({form_key})</h3>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            height = st.number_input("身高 (cm):", min_value=0.0, step=0.1, key=height_key)
            weight = st.number_input("體重 (kg):", min_value=0.0, step=0.1, key=weight_key)

        with col2:
            st.markdown('<br>', unsafe_allow_html=True)
            if session_flag:
                bmi_cal = st.form_submit_button("開始計算")
                st.markdown('<br>', unsafe_allow_html=True)
                bmi_clear = st.form_submit_button("清除結果")
            else:
                st.form_submit_button("開始計算", on_click=cal_callback, args=(col3,))
                st.markdown('<br>', unsafe_allow_html=True)
                st.form_submit_button("清除結果", on_click=clear_callback, args=(col3,))

        with col3:
            if session_flag:
                if bmi_cal:
                    if st.session_state[weight_key] <= 0 or st.session_state[height_key] <= 0:
                        st.markdown("<br><br>", unsafe_allow_html=True)
                        st.error("輸入值不可為負值或零，請重新輸入。")
                    else:
                        bmi = st.session_state[weight_key] / ((st.session_state[height_key] / 100) ** 2)
                        if bmi < 18.5:
                            txt = "<font color=DarkBlue>**體重過輕**</font>"
                        elif bmi < 24:
                            txt = "<font color=green>**正常範圍**</font>"
                        elif bmi < 27:
                            txt = "<font color=red>**過重**</font>"
                        elif bmi < 30:
                            txt = "<font color=Fuchsia>**輕度肥胖**</font>"
                        elif bmi < 35:
                            txt = "<font color=DarkSalmon>**中度肥胖**</font>"
                        else:
                            txt = "<font color=BlueViolet>**重度肥胖**</font>"

                        st.markdown("<br><br>", unsafe_allow_html=True)
                        st.markdown(f"您的BMI值為: {bmi:.2f} <br> 體重: {txt}", unsafe_allow_html=True)

                if bmi_clear:
                    st.session_state.weight_key = 0.0
                    st.session_state.height_key = 0.0
                    #為何不能將st.session_state.weight_input_1設定為0.0???
                    #st.session_state[weight_key] = 0.0
                    #st.session_state[height_key] = 0.0
                    #print(st.session_state.weight_input_1)
                    #st.experimental_rerun()

# 使用 tabs 來顯示兩個表單
tab1, tab2 = st.tabs(["session_state", "call_back"])

# session_state 方式
with tab1:
    display_bmi_form("session_state", "weight_input_1", "height_input_1",session_flag=True)
    BMI_info()

# call_back 方式
with tab2:
    display_bmi_form("call_back", "weight_input_2", "height_input_2", session_flag=False)
    BMI_info()