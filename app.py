import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    """Fetches the movie poster URL from TMDb API."""
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url, timeout=10)  # Set timeout
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"  # Placeholder image
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    """Returns top 5 recommended movies and their posters."""
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])

        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:  # Get top 5 recommendations
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_names.append(movies.iloc[i[0]].title)
            recommended_movie_posters.append(fetch_poster(movie_id))

        return recommended_movie_names, recommended_movie_posters
    except Exception as e:
        st.error(f"Error in recommendation: {e}")
        return [], []

# Streamlit UI
st.header('Movie Recommender System 🎬 ')

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Show recommendations on button click
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    if recommended_movie_names:
        cols = st.columns(5)  # Use st.columns() instead of deprecated st.beta_columns()
        for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
            with col:
                st.text(name)
                st.image(poster)
    else: 
        st.warning("No recommendations found.")
