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
    
    # Initialize session state for both images
    if "show_image1" not in st.session_state:
        st.session_state.show_image1 = False
    if "show_image2" not in st.session_state:
        st.session_state.show_image2 = False
    
    # Button for first image
    if st.button("Meme 1"):
        st.session_state.show_image1 = not st.session_state.show_image1
    
    # Button for second image
    if st.button("Meme 2"):
        st.session_state.show_image2 = not st.session_state.show_image2
    
    # Show images conditionally
    if st.session_state.show_image1:
        st.image("https://www.theinsaneapp.com/wp-content/uploads/2024/10/Data-Science-Meme-7.png", caption = 'Meme')
    
    if st.session_state.show_image2:
        st.image("https://www.atoti.io/wp-content/uploads/2024/06/1_t4zCD60p-dDd5BRmINW9tQ.webp", caption = 'Meme')

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
