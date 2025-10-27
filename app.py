import pickle
import streamlit as st

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_name, movies_df=movies, similarity_matrix=similarity):
    """Movie-based recommendation: top 5 similar movies."""
    if movie_name not in movies_df['title'].values:
        return [f"Movie '{movie_name}' not found."]
    idx = movies_df[movies_df['title'] == movie_name].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_5_idx = [i[0] for i in sim_scores[1:6]]
    return movies_df.iloc[top_5_idx]['title'].tolist()

def recommend_by_mood(movie_name, mood_keywords, movies_df=movies, similarity_matrix=similarity):
    """Mood/keyword-based recommendation: filter top 5 similar movies by keywords."""
    if movie_name not in movies_df['title'].values:
        return [f"Movie '{movie_name}' not found."]
    idx = movies_df[movies_df['title'] == movie_name].index[0]
    sim_scores = sorted(list(enumerate(similarity_matrix[idx])), key=lambda x: x[1], reverse=True)
    
    recommended_movies = []
    for i in sim_scores[1:]:
        movie_tags = movies_df.iloc[i[0]]['tags'].lower()
        if any(keyword.lower() in movie_tags for keyword in mood_keywords):
            recommended_movies.append(movies_df.iloc[i[0]]['title'])
        if len(recommended_movies) == 5:
            break
    return recommended_movies

def recommend_creative(movie_name, movies_df=movies, similarity_matrix=similarity,
                       genre_weight=0.5, cast_weight=0.3, keyword_weight=0.2):
    """Creative weighted recommendation: weighted genres, cast, keywords."""
    idx = movies_df[movies_df['title'] == movie_name].index[0]
    similarities = similarity_matrix[idx]
    weighted_sim = similarities * (genre_weight + cast_weight + keyword_weight)
    recommended_indices = sorted(enumerate(weighted_sim), key=lambda x: x[1], reverse=True)[1:6]
    return [movies_df.iloc[i[0]]['title'] for i in recommended_indices]

st.title("🎬 Movie Recommendation System")

rec_type = st.selectbox(
    "Select Recommendation Type:",
    ['Movie-Based', 'Mood/Keyword-Based', 'Creative Weighted']
)


selected_movie = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

mood_options = ['Action', 'Comedy', 'Romance', 'Drama', 'Adventure', 'Fantasy', 'Horror', 'Animation', 'Family', 'Thriller', 'Mystery', 'Sci-Fi', 'Superhero', 'Crime', 'Musical', 'Magic', 'Inspirational']
selected_moods = []
if rec_type == 'Mood/Keyword-Based':
    selected_moods = st.multiselect("Select mood/keywords:", mood_options, default=['Action', 'Adventure'])

if st.button("Show Recommendations"):
    if rec_type == 'Movie-Based':
        recommendations = recommend(selected_movie)
    elif rec_type == 'Mood/Keyword-Based':
        recommendations = recommend_by_mood(selected_movie, selected_moods)
    elif rec_type == 'Creative Weighted':
        recommendations = recommend_creative(selected_movie)
    
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write(f"▶️ {movie}")


st.markdown(
   "<p style='text-align: center; font-size:14px;'> Made with 💡 by <b>Ankit Sarkar</b></p>",
   unsafe_allow_html=True
)
