import streamlit as st
import pandas as pd
import numpy as np

st.title("Would you survive the Titanic disaster?")

with st.form(key="titanic_form"):
    # Creating a button to select First Class, Second Class, Third Class
    passenger_class = st.selectbox("What passenger class are you?", ['First Class', 'Second Class', 'Third Class'])
    
    # Creating a button to select gender (male or female)
    gender = st.selectbox("What is your gender?", ['Male', 'Female'])
    
    # Creating age slider
    age_slider = st.slider('How old are you?', 0, 80)
    
    # Creating sibling/spouses slider
    sib_spouse_slider = st.slider('How many siblings and spouses were with you?', 0, 8)
    
    # Creating parents/children slider
    parent_child_slider = st.slider('How many parents and children were aboard with you?', 0, 6)
    
    # Creating how much you paid slider
    payment_slider = st.slider('How much did you pay for your cruise ticket? (in 1910 USD)', 14, 512)
    
    # Creating a button to select port
    port = st.selectbox("Which port did you embark from?", ['Cherbourg', 'Queenstown', 'Southampton'])
    
    #Creating Submit and Reset buttons
    col1, col2 = st.columns(2)
    with col1:
        submit_button = st.form_submit_button("Submit")
    with col2:
        reset_button = st.form_submit_button("Reset")
    
if submit_button:
    st.success("Form submitted successfully!")
    st.write("### Submitted Responses")
    st.write(f"**Passenger Class:** {passenger_class}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Age:** {age_slider}")
    st.write(f"**Siblings/Spouses Aboard:** {sib_spouse_slider}")
    st.write(f"**Parents/Children Aboard:** {parent_child_slider}")
    st.write(f"**Ticket Price:** {payment_slider} (1910 USD)")
    st.write(f"**Port of Embarkation:** {port}")

if reset_button:
    st.warning("Form reset. Please enter your details again.")
