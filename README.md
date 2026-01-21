📚 Book Recommender System using Machine Learning

A content-based Book Recommendation System built using Machine Learning and deployed using Streamlit Cloud.
This application recommends similar books based on user selection using a KNN model.

🚀 Live Demo

👉https://book-recommender60.streamlit.app/
🧠 Project Overview

This project uses collaborative filtering techniques to recommend books.
It calculates similarity between books using user ratings and suggests the most relevant books along with their cover images.

🛠️ Tech Stack

Python

Streamlit

NumPy

Pandas

Scikit-learn

Pickle

Git & GitHub

📂 Project Structure
book-recommender/
│
├── src/
│   └── app.py               # Streamlit application
│
├── artifacts/
│   ├── model.pkl            # Trained KNN model
│   ├── books_name.pkl       # Book names
│   ├── final_rating.pkl     # Ratings data
│   └── book_pivot.pkl       # Pivot table
│
├── requirements.txt         # Python dependencies
├── setup.sh                 # Streamlit Cloud config
├── .gitignore
├── README.md



⚙️ How It Works

User selects a book from the dropdown.

The model finds similar books using K-Nearest Neighbors.

Recommended books and their posters are displayed.

Recommendations are based on similarity in user ratings.

▶️ Run Locally
1️⃣ Clone the repository
git clone https://github.com/lilavatipandit/book-recommender.git
cd book-recommender

2️⃣ Create virtual environment (optional but recommended)
python -m venv env
env\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the app
streamlit run src/app.py

🌐 Deployment (Streamlit Cloud)

Push code to GitHub

Go to https://share.streamlit.io/

Select:

Repository: lilavatipandit/book-recommender

Branch: main

Main file path: src/app.py

Click Deploy

📌 Features

Interactive UI using Streamlit

Fast recommendations using KNN

Displays book cover images

Easy deployment on Streamlit Cloud

Beginner-friendly ML project

📊 Dataset

Book-Crossing Dataset

Contains:

Users

Books

Ratings

👩‍💻 Author

Lilavati Pandit

💻 Web & Backend Developer

📊 Machine Learning Enthusiast

🌱 Always learning & growing

🔗 GitHub: https://github.com/lilavatipandit

⭐ If you like this project

Give it a star ⭐ on GitHub — it motivates me to build more!

