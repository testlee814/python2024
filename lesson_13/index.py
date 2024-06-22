import streamlit as st

st.subheader("BMI calculator")
st.divider()
st.latex( 'BMI calculator: BMI = weight(kg) / height^2(cm^2)')
st.latex('For example, if you are 52 kg, height is 155 cm, then your BMI is:')

st.markdown('<h6 style="color:blue;text-align:center">\
            52(公斤) / 1.552 ( 公尺<sup>2</sup> ) = 21.6</h6>', 
            unsafe_allow_html=True)
##如果想斷行 後面要加\

st.markdown('<h6 style="color:orange;text-align:center">體重正常範圍為 BMI = 18.5～24</h6>', 
            unsafe_allow_html=True)
st.markdown('<hr style="border:0;margin:0 auto;width:80%;border-top:2px dotted blue">', 
            unsafe_allow_html=True)
st.markdown('<h6 style="color:purple;text-align:center">快看看自己的BMI是否在理想範圍吧!</h6>', 
            unsafe_allow_html=True)
