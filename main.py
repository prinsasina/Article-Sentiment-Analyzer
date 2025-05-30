from textblob import TextBlob
from newspaper import Article
import streamlit as st
import matplotlib.pyplot as plt

st.title("SentimentScope")
st.write("Text & Articles Sentiment Dashboard")

mode = st.radio("Select input method:", ["URL","Text"])

if mode == "URL":
    url = st.text_input("Enter the URL: ")

    if st.button("Analyze"):
        if url:
            try:
                article = Article(url)

                article.download()
                article.parse()
                article.nlp()

                st.subheader("Article Summary")
                text = article.summary
                st.write(text)

                st.subheader("Sentiment Polarity")
                blob = TextBlob(text)
                sentiment = round(blob.sentiment.polarity * 100, 2)
                st.write(f"{sentiment}%")

                graph, axis = plt.subplots()
                axis.bar(["Sentiment"],[sentiment], color="red")
                axis.set_ylim([-100,100])
                axis.set_ylabel("Polarity (%)")
                st.pyplot(graph)
            
            except Exception:
                st.error("Failed to process the URL")

elif mode == "Text":
    text_input = st.text_input("Enter the text: ")

    if st.button("Analyze"):
        if text_input:
            try:
                st.subheader("Text")
                st.write(text_input)

                st.subheader("Sentiment Polarity")
                blob = TextBlob(text_input)
                sentiment = round(blob.sentiment.polarity * 100, 2)
                st.write(f"{sentiment}%")

                graph, axis = plt.subplots()
                axis.bar(["Sentiment"],[sentiment], color="red")
                axis.set_ylim([-100,100])
                axis.set_ylabel("Polarity (%)")
                st.pyplot(graph)
            
            except Exception:
                st.error("Failed to process the text")