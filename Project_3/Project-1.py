from bs4 import BeautifulSoup
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def extract_products(soup):
    products = []
    product_elements = soup.find_all(name="div", class_="product")
    for product in product_elements:
        Name = product.find("h1").text
        Company = product.find("h2").text
        Model = product.find("h3").text
        products.append({"Name": Name, "Company": Company, "Model": Model})
    return products

def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
        return "Positive ☺️️"
    elif sentiment < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)["compound"]

    if sentiment > 0.05:
        return "Positive ☺️"
    elif sentiment < -0.05:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def main():
    html_content = load_html("Electronics store.html")
    soup = BeautifulSoup(html_content, "html.parser")
    products = extract_products(soup)

    print("===== Electronics Items =====")
    for product in products:
        print(f"Name: {product['Name']}")
        print(f"Company: {product['Company']}")
        print(f"Model: {product['Model']}")
        print("-----------------------------")

    feedback = input("Enter your feedback about the cars: ")

    print("\n===== FEEDBACK SENTIMENT =====")
    print(f"TextBlob Sentiment: {analyze_sentiment_textblob(feedback)}")
    print(f"Vader Sentiment: {analyze_sentiment_vader(feedback)}")

def analyze_input():
    text = input("Enter a sentence for analysis:")
    print(f"TextBlob Sentiment: {analyze_sentiment_textblob(text)}")
    print(f"Vader Sentiment: {analyze_sentiment_vader(text)}")

    analyze_input()

if __name__ == "__main__":
    main()