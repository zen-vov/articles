from flask import Flask, jsonify
from flask_cors import CORS
from articles import fetchArticles, getWordCount

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/articles')
def get_articles():
    keywords = ["burger", "banana", "javascript"]
    all_articles = []

    for keyword in keywords:
        articles = fetchArticles(keyword)
        if articles:
            for article in articles:
                title = article['title']
                description = article['description'] or ""
                content = article['content'] or ""
                full_text = f"{title}. {description} {content}"
                word_freq = getWordCount(full_text)
                article_data = {
                    'title': title,
                    'description': description,
                    'content': content,
                    'word_frequency': dict(word_freq)
                }
                all_articles.append(article_data)

    return jsonify({'articles': all_articles})

if __name__ == '__main__':
    app.run(debug=True)
