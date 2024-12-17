import streamlit as st 
import pickle
import pandas as pd


def recammand(movie):
    if movie not in movies['title'].values:
        print(f"Error: Movie '{movies}' not found in the dataset.")
        return []
    movie_index=movies[movies['title'] == movie].index[0]
    
    distance=similarity[movie_index]
    
    movie_list=sorted(list(enumerate(distance)),reverse=True,key =lambda x:x[1])[1:6]
    
    recammadation_list=[]
    for i in movie_list:
        recammadation_list.append(movies.iloc[i[0]].title)
    return recammadation_list


# Open the file in 'rb' mode and load the dictionary
with open("movies.pkl", "rb") as file:
    movies_dict = pickle.load(file)
with open("similarity.pkl", "rb") as file:
    similarity = pickle.load(file)

movies=pd.DataFrame(movies_dict)

st.title("Movie Recommendation System")


selected_movie = st.selectbox(
    "How would you like to be contacted?",
    movies["title"].values,
)



if st.button("recammed"):
    recammand_list = recammand(selected_movie)
    st.write("### Recommended Movies:")
    for movie in recammand_list:
        st.write(f"- {movie}")
