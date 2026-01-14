# # import pickle
# # import streamlit as st
# # import numpy as np

# # st.header("Books Recommender System using Machine Learning")

# # # Load model and data
# # model = pickle.load(open('../artifacts/model.pkl', 'rb'))
# # books_name = pickle.load(open('../artifacts/books_name.pkl', 'rb'))
# # final_rating = pickle.load(open('../artifacts/final_rating.pkl', 'rb'))
# # book_pivot = pickle.load(open('../artifacts/book_pivot.pkl', 'rb'))

# # st.subheader("Select a Book")

# # selected_book = st.selectbox(
# #     "Choose a book",
# #     books_name
# # )

# # def recommend(book_name):
# #     index = np.where(book_pivot.index == book_name)[0][0]
# #     distances, suggestions = model.kneighbors(
# #         book_pivot.iloc[index].values.reshape(1, -1),
# #         n_neighbors=6
# #     )

# #     recommended_books = []
# #     for i in suggestions[0][1:]:
# #         recommended_books.append(book_pivot.index[i])

# #     return recommended_books

# # if st.button("Recommend"):
# #     recommendations = recommend(selected_book)
# #     st.subheader("Recommended Books:")
# #     for book in recommendations:
# #         st.write(book)
# def fetch_poster(suggestion):
#     book_name = []
#     ids_index = []
#     poster_url = []

#     for book_id in suggestion[0]:
#         book_name.append(book_pivot.index[book_id])

#     for name in book_name:
#         ids = np.where(final_rating['title'] == name)[0][0]
#         ids_index.append(ids)

#     for idx in ids_index:
#         url = final_rating.iloc[idx]['img_url']
#         poster_url.append(url)

#     return poster_url


# def recommend_books(book_name):
#     book_list = []

#     book_id = np.where(book_pivot.index == book_name)[0][0]

#     distances, suggestion = model.kneighbors(
#         book_pivot.iloc[book_id, :].values.reshape(1, -1),
#         n_neighbors=6
#     )

#     poster_url = fetch_poster(suggestion)

#     for i in suggestion[0]:
#         book_list.append(book_pivot.index[i])

#     return book_list, poster_url


# selected_books = st.selectbox(
#     "Type or select a book",
#     books_name
# )

# if st.button("Show Recommendation"):

#     recommendation_books, poster_url = recommend_books(selected_books)

#     col1, col2, col3, col4, col5 = st.columns(5)

#     with col1:
#         st.text(recommendation_books[1])
#         st.image(poster_url[1])

#     with col2:
#         st.text(recommendation_books[2])
#         st.image(poster_url[2])

#     with col3:
#         st.text(recommendation_books[3])
#         st.image(poster_url[3])

#     with col4:
#         st.text(recommendation_books[4])
#         st.image(poster_url[4])

#     with col5:
#         st.text(recommendation_books[5])
#         st.image(poster_url[5])
import pickle
import streamlit as st
import numpy as np

# Page title
st.set_page_config(page_title="Book Recommender", layout="wide")
st.header("📚 Book Recommender System using Machine Learning")

# Load model files
model = pickle.load(open("../artifacts/model.pkl", "rb"))

books_name = pickle.load(open("../artifacts/books_name.pkl", "rb"))
final_rating = pickle.load(open("../artifacts/final_rating.pkl", "rb"))
book_pivot = pickle.load(open("../artifacts/book_pivot.pkl", "rb"))

# Convert books_name to list
if hasattr(books_name, "values"):
    books_name = books_name.values.tolist()

# ============================
# Fetch Poster Function
# ============================
def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion[0]:
        book_name.append(book_pivot.index[book_id])

    for name in book_name:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url


# ============================
# Recommendation Function
# ============================
def recommend_books(book_name):
    book_list = []

    book_id = np.where(book_pivot.index == book_name)[0][0]

    distance, suggestion = model.kneighbors(
        book_pivot.iloc[book_id, :].values.reshape(1, -1),
        n_neighbors=6
    )

    poster_url = fetch_poster(suggestion)

    for i in range(1, 6):
        book_list.append(book_pivot.index[suggestion[0][i]])

    return book_list, poster_url


# ============================
# Streamlit UI
# ============================

selected_books = st.selectbox(
    "Type or select a book",
    books_name
)

if st.button("Show Recommendation"):
    recommended_books, poster_url = recommend_books(selected_books)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_books[0])
        st.image(poster_url[1])

    with col2:
        st.text(recommended_books[1])
        st.image(poster_url[2])

    with col3:
        st.text(recommended_books[2])
        st.image(poster_url[3])

    with col4:
        st.text(recommended_books[3])
        st.image(poster_url[4])

    with col5:
        st.text(recommended_books[4])
        st.image(poster_url[5])
