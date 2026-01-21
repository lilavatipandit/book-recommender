# 📚 Book Recommender System using Machine Learning

A **content-based Book Recommendation System** built using **Machine Learning** and deployed using **Streamlit Cloud**.  
This application recommends similar books based on user selection using a **KNN model**.

---

## 🚀 Live Demo

👉 https://book-recommender60.streamlit.app/

---

## 🧠 Project Overview

This project uses **collaborative filtering techniques** to recommend books.  
It calculates similarity between books using user ratings and suggests the most relevant books along with their cover images.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- NumPy
- Pandas
- Scikit-learn
- Pickle
- Git & GitHub

---

## 📂 Project Structure
## 📂 Project Structure

book-recommender/
├── src/
│ └── app.py # Streamlit application
├── artifacts/
│ ├── model.pkl # Trained KNN model
│ ├── books_name.pkl # Book names
│ ├── final_rating.pkl # Ratings data
│ └── book_pivot.pkl # Pivot table
├── requirements.txt
├── setup.sh
├── .gitignore
└── README.md

⚠️ VERY IMPORTANT RULES

book-recommender/
├── src/
│ └── app.py # Streamlit application
├── artifacts/
│ ├── model.pkl # Trained KNN model
│ ├── books_name.pkl # Book names
│ ├── final_rating.pkl # Ratings data
│ └── book_pivot.pkl # Pivot table
├── requirements.txt
├── setup.sh
├── .gitignore
└── README.md








---

## ⚙️ How It Works

1. User selects a book from the dropdown
2. Model finds similar books using **KNN**
3. Book posters and titles are displayed
4. Recommendations are based on rating similarity

---

## ▶️ Run Locally

```bash
git clone https://github.com/lilavatipandit/book-recommender.git
cd book-recommender
pip install -r requirements.txt
streamlit run src/app.py

🌐 Deployment

Deployed using Streamlit Cloud

Repository: lilavatipandit/book-recommender

Branch: main

Main file: src/app.py

👩‍💻 Author

Lilavati Pandit
GitHub: https://github.com/lilavatipandit





