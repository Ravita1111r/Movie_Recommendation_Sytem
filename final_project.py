import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_pic(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x : x[1])[1:6]
  
  rec_movies=[]
  rec_movies_posters=[]
  for i in movies_list:
      movie_id = movies.iloc[i[0]].movie_id
      rec_movies.append(movies.iloc[i[0]].title)
      rec_movies_posters.append(fetch_pic(movie_id))
  
  return rec_movies,rec_movies_posters 
    
movies_list=pickle.load(open('C:\\Users\\satya\\Movie_rec_system\\movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)

similarity=pickle.load(open('C:\\Users\\satya\\Movie_rec_system\\similarity.pkl','rb'))
st.title('Movie recommender system')

select_movie_name = st.selectbox(
    'Enter the name of movie',movies['title'].values
    )

if st.button('Recommend'):
    names,pics=recommend(select_movie_name)
    
    a1,a2,a3,a4,a5 = st.columns(5)
    with a1:
        st.text(names[0])
        st.image(pics[0])
    with a2:
        st.text(names[1])
        st.image(pics[1])
    with a3:
        st.text(names[2])
        st.image(pics[2])
    with a4:
        st.text(names[3])
        st.image(pics[3])
    with a5:
        st.text(names[4])
        st.image(pics[4])    
        
        
#8265bd1679663a7ea12ac168da84d2e8        
