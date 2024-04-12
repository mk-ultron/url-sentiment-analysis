# url-sentiment-analysis
This program is a Streamlit web application that performs sentiment analysis on the text content of a user-provided URL. It analyzes the sentiment of the website's text and determines whether the overall sentiment is positive, negative, or neutral.

## Features

- User-friendly web interface built with Streamlit
- Accepts a URL input from the user
- Fetches the web page content using the Requests library
- Extracts the text content from the HTML using BeautifulSoup
- Performs sentiment analysis on the extracted text using TextBlob
- Displays the sentiment analysis results, including the overall sentiment and sentiment score

## Requirements

- Python 3.x
- Streamlit
- Requests
- BeautifulSoup4
- TextBlob

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/website-sentiment-analysis.git
   ```

2. Navigate to the project directory:

   ```
   cd website-sentiment-analysis
   ```

3. Install the required libraries:

   ```
   pip install streamlit requests beautifulsoup4 textblob
   ```

## Usage

1. Run the Streamlit app:

   ```
   streamlit run website_sentiment_analysis.py
   ```

2. Open the provided URL in your web browser.

3. Enter a valid URL in the input field.

4. Click the "Analyze" button to perform sentiment analysis on the website's text content.

5. The program will display the sentiment analysis results, indicating whether the overall sentiment is positive, negative, or neutral, along with the sentiment score.

## Example

Here's an example of how to use the Website Sentiment Analysis program:

1. Run the Streamlit app:

   ```
   streamlit run website_sentiment_analysis.py
   ```

2. Open the provided URL in your web browser.

3. Enter a URL, for example, `https://www.example.com`.

4. Click the "Analyze" button.

5. The program will fetch the web page content, extract the text, perform sentiment analysis, and display the results.

   Example output:
   ```
   Sentiment Analysis Results
   The overall sentiment of the website is positive.
   Sentiment Score: 0.8
   ```

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [TextBlob](https://textblob.readthedocs.io/)

Feel free to customize the README file according to your specific project details and requirements.
