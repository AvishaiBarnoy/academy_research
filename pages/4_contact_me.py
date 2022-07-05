import streamlit as st

st.markdown("""
        # Under construction
        This will be different than my twitter account and will probably include a form
        """)
with st.form("my_form", clear_on_submit=True):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    title = st.text_input(label="Message title")
    text = st.text_input(label="Your message",value="")
  
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
   
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
        st.write('User Input', text)
