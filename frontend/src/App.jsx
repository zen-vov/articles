import React, { useState, useEffect } from "react";
import "./App.css";
import ArticleList from "./components/articlesList";

function App() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    fetchArticles();
  }, []);

  const fetchArticles = async () => {
    try {
      const res = await fetch("http://localhost:5000/articles");
      if (!res.ok) {
        throw new Error("Ошибка при запросе");
      }
      const data = await res.json();
      setArticles(data.articles);
    } catch (error) {
      console.error("Ошибка:", error.message);
    }
  };

  return (
    <main className="main">
      <h1>Статейки короче</h1>
      <ArticleList articles={articles} />
    </main>
  );
}

export default App;
