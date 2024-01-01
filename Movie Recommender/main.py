import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender")
selectValue = st.selectbox("Select movie from dropdown", movies_list)


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)

    return recommend_movie


if st.button("Show recommended movies"):
    movies_names = recommend(selectValue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movies_names[0])
    with col2:
        st.text(movies_names[1])
    with col3:
        st.text(movies_names[2])
    with col4:
        st.text(movies_names[3])
    with col5:
        st.text(movies_names[4])
