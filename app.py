import streamlit as st

import pickle


# def fetch_posters(moive_id):
#     pass


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        # movie_id = i[1]
        # fetch_posters(movie_id)
        recommended_movies.append(movies.iloc[i[0]].title)
        # print(movies.iloc[i[0]].title)
    return recommended_movies

with open("model.pkl", "rb") as f:
    movies = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

st.title("Movie Recommender System")

movies_list = movies['title'].values



selected_movie_name = st.selectbox("Select a movie", 
                      movies_list)

if st.button('Recommend'):
    st.write("You have selected: ", selected_movie_name)
    st.write("Here are the top 5 similar movies")
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

