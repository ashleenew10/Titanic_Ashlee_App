import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open("titanic_predictor.sav", "rb") as file:
    model = pickle.load(file)

# Function to make predictions
def predict_survival(model, features):
    features = np.array(features).reshape(1, -1)  # Ensure correct shape
    prediction = model.predict(features)
    return "Survived" if prediction[0] == 1 else "Did Not Survive"

# Streamlit app
def main():
    st.title("Would you survive the Titanic disaster?")
    st.write("Enter the details below to predict survival on the Titanic:")

    # Input fields
    Pclass_mapping = {'First Class': 1, 'Second Class': 2, 'Third Class': 3}
    Pclass = st.selectbox("What passenger class are you?", list(Pclass_mapping.keys()))
    Pclass = Pclass_mapping[Pclass]  # Convert to numeric

    Gender = st.selectbox("What is your gender?", ['Male', 'Female'])
    Age = st.slider('How old are you?', 0, 80)
    SibSp = st.slider('How many siblings and spouses were with you?', 0, 8)
    Parch = st.slider('How many parents and children were aboard with you?', 0, 6)
    Fare = st.slider('How much did you pay for your cruise ticket? (in 1910 USD)', 0, 512)

    # Convert gender to numeric
    Sex = 1 if Gender == "Female" else 0

    # Prepare features for prediction
    features = [Pclass, Sex, Age, SibSp, Parch, Fare]

    # Prediction
    if st.button("Predict"):
        result = predict_survival(model, features)
        st.write(f"Prediction: {result}")

if __name__ == "__main__":
    main()
