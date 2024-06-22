import streamlit as st

st.subheader("BMI calculator")
st.divider()
st.latex( 'BMI calculator: BMI = weight(kg) / height^2(cm^2)')
st.latex('For example, if you are 52 kg, height is 155 cm, then your BMI is:')

st.markdown('<h6 style="color:blue;text-align:center">\
            52(公斤) / 1.552 ( 公尺<sup>2</sup> ) = 21.6</h6>', 
            unsafe_allow_html=True)
##如果想斷行 後面要加\
 
st.markdown('<hr style="border:0;margin:0 auto;width:80%;border-top:2px dotted green">', 
            unsafe_allow_html=True)
st.markdown('<h6 style="color:purple;text-align:center">快看看自己的BMI是否在理想範圍吧!</h6>', 
            unsafe_allow_html=True)

if 'bmi_result' not in st.session_state:
    st.session_state.bmi_result = 0

with st.form('bmi form',border=False):
    height = st.slider(":green[Choose your height(cm)]",max_value=250,min_value=100,key="height")
    weight = st.number_input(":green[Choose your weight(kg)]",max_value=200,min_value=30,key="weight")
    txt=''
    if st.form_submit_button("BMI calculator Go!"):
        st.session_state.bmi_result = round(weight/(height/100)**2,1)
        if st.session_state.bmi_result <18.5:
            txt = "體重過輕"
        elif st.session_state.bmi_result < 24:
            txt = "正常範圍"
        elif st.session_state.bmi_result < 27:
            txt = "過重"
        elif st.session_state.bmi_result < 30:
            txt = "輕度肥胖"
        elif st.session_state.bmi_resultsult < 35:
            txt = "中度肥胖"
        else:
            txt = "重度肥胖"
    
st.markdown(f'## :red[{st.session_state.bmi_result}]')
st.markdown(f'### :red[{txt}]')


 
st.session_state

 