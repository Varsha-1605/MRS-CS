import streamlit as st
import compress_pickle



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



movies = compress_pickle.load("model.pkl.gz", compression="gzip")
similarity = compress_pickle.load("similarity.pkl.gz", compression="gzip")


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

