# Movie-Recommendation-System

Movie Recommendation System Web-App : [Movie Recommendation System](https://movie-recommendation-system-ankitsarkar.streamlit.app/)

Dataset: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data)

INTRODUCTION :

A personalized Movie Recommendation System that suggests movies based on your favorite films, moods, or themes and it combines movie metadata, cast, genres, and keywords to provide smart, interactive recommendations.

UNIQUE FEATURES :

+ Mood/keyword filtering enables theme-based discovery.

+ Creative weighted recommendations boost recent movies and combine multiple metadata features.

+ Fully deployable on Streamlit with interactive UI for user-friendly experience.

WORKFLOW :

1) Data Processing ---

  + Datasets: tmdb_5000_movies.csv and tmdb_5000_credits.csv
+ Steps:

  +Merge movies and credits datasets on title.

  +Handle missing values by dropping incomplete rows.

  +Extract features:

      +Genres → List of genres for each movie.

      +Keywords → List of keywords from metadata.

      +Cast → Top 3 cast members.

      +Crew → Director names.

      +Overview → Split into words.

  +Combine all textual info into a single tags column for vectorization.

  +Save processed dataframe and similarity matrix as pickle files for deployment.

2) Model Concepts & Features ---

=> TF-IDF Vectorization :

    -Input: tags column (combined textual info)

    -Process: Converts movie text data into numerical feature vectors.

    -Output: TF-IDF matrix representing each movie.

=> Cosine Similarity :

     -Input: TF-IDF matrix

     -Process: Measures similarity between movies based on vector representations.

     -Output: Similarity matrix used for recommendation ranking.

3) Recommendation Features ---
   
   Movie-Based Recommendation

       = Input: Movie name

       = Processing: Finds the index of the movie in the dataset and retrieves top 5 movies based on cosine similarity.

       = Output: List of top 5 similar movies.

   Mood/Keyword-Based Recommendation

       = Input: Movie name + list of mood/keywords

       = Processing: Retrieves movies similar to the input movie, filtered to include selected keywords in the tags.

       = Output: Top 5 movies matching the mood or keyword criteria.

   Creative Weighted Recommendation

       = Input: Movie name

       = Processing: Applies weighted scores for genres, cast, and keywords; optionally boosts recent releases for fresher recommendations.

       = Output: Top 5 recommended movies based on the weighted combination.
   
4) Results ---

+ Movie-Based: Suggests movies highly similar in genre, cast, and storyline.

+ Mood/Keyword-Based: Allows exploring movies aligned with specific moods, genres, or themes.

+ Creative Weighted: Offers unique recommendations factoring multiple attributes and recency, giving users a richer and more diverse set of movie suggestions.
