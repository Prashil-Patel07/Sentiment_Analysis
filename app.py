import streamlit as st
import pandas as pd
import joblib
from utils import preprocessor

def run():
    model = joblib.load(open('model.joblib','rb'))

    st.title("Sentiment Analysis")
    st.text("Basic app to detect the sentiment of text.")
    st.text("")
    userinput = st.text_input('Enter text below, then click the Predict button.', placeholder='Input text HERE')
    st.text("")
    if "show_image" not in st.session_state:
        st.session_state.show_image = False

    if st.button("Click me to toggle image"):
        st.session_state.show_image = not st.session_state.show_image

    if st.session_state.show_image:
        st.image("https://www.atoti.io/wp-content/uploads/2024/06/1_t4zCD60p-dDd5BRmINW9tQ.webp")

    if "show_image" not in st.session_state:
        st.session_state.show_image = False

    if st.button("Click me to toggle image"):
        st.session_state.show_image = not st.session_state.show_image

    if st.session_state.show_image:
        st.image("https://www.theinsaneapp.com/wp-content/uploads/2024/10/Data-Science-Meme-7.png")

    predicted_sentiment = ""
    if st.button("Predict"):
        predicted_sentiment = model.predict(pd.Series(userinput))[0]
        if predicted_sentiment == 1:
            output = 'positive 👍'
        else:
            output = 'negative 👎'
        sentiment=f'Predicted sentiment of "{userinput}" is {output}.'
        st.success(sentiment)

if __name__ == "__main__":
    run()
