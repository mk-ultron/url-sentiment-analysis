import streamlit as st
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Streamlit app
def main():
    st.title("URL Sentiment Analysis")
    st.write("This program analyzes the sentiment of the text content on a user-provided URL and marks the intent as positive or negative.")
    st.write("To use the program, enter a valid URL in the input field below and click the 'Analyze' button.")

    # User input
    url = st.text_input("Enter a URL:")

    if st.button("Analyze"):
        if url:
            try:
                # Fetch the web page content
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")

                # Extract the text content
                text = soup.get_text()

                # Perform sentiment analysis
                analysis = TextBlob(text)
                sentiment = analysis.sentiment.polarity

                # Display results
                st.subheader("Sentiment Analysis Results")
                if sentiment > 0:
                    st.write("The overall sentiment of the website is positive.")
                elif sentiment < 0:
                    st.write("The overall sentiment of the website is negative.")
                else:
                    st.write("The overall sentiment of the website is neutral.")

                st.write(f"Sentiment Score: {sentiment}")

            except requests.exceptions.RequestException as e:
                st.error("Error occurred while fetching the URL. Please check the URL and try again.")
        else:
            st.warning("Please enter a valid URL.")

if __name__ == "__main__":
    main()
