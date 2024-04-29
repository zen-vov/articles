import React from "react";

function ArticleList({ articles }) {
  return (
    <div className="article-list">
      {articles.map((article, index) => (
        <div key={index} className="article">
          <h2>{article.title}</h2>
          <p>{article.description}</p>
          <p>{article.content}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default ArticleList;
