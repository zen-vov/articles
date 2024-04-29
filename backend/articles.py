import requests
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

key = '9223811d071444c694978a57386cb671'

def fetchArticles(keyword):
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={key}'
    res = requests.get(url)
    if res.status_code == 200:
        data = json.loads(res.text)
        articles = data['articles']
        return articles
    else:
        print(f"Ошибка при запросе: {res.status_code}")
        return []

def getWordCount(text):
    tokens = word_tokenize(text)
    stopWords = set(stopwords.words('english'))
    filteredTokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stopWords]
    wordFreq = Counter(filteredTokens)
    return wordFreq

def printArticles(keywords):
    for keyword in keywords:
        print(f"Мониторинг: '{keyword}':")
        articles = fetchArticles(keyword)
        if articles:
            for article in articles:
                title = article['title']
                description = article['description'] or ""
                content = article['content'] or ""
                fullText = f"{title}. {description} {content}"
                wordFreq = getWordCount(fullText)
                print(f"Заголовок: {title}")
                print(f"Частота слов: {wordFreq}")
                print(f"Контент: {fullText}")
                print("-------------------------------------\n\n\n")
        else:
            print(f"Нет статей")
        print("\n")

if __name__ == "__main__":
    keywords = ["burger", "banana", "javascript"]
    printArticles(keywords)
