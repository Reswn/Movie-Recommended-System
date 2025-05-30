import streamlit as st
import pickle
import requests

# Load data dan model
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# =================== Styling ===================
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: 800;
        text-align: center;
        color: #28a745;  /* Hijau cerah */
        margin-bottom: 30px;
        font-family: 'Segoe UI', sans-serif;
    }

    .movie-card {
        padding: 10px;
        background-color: #ffffff;
        border: 2px solid #28a745;  /* Bingkai hijau */
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);  /* Bayangan hijau transparan */
        transition: transform 0.2s ease, box-shadow 0.3s ease;
        margin: 10px 5px;
        height: 100%;
        text-align: center;
    }

    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(40, 167, 69, 0.5);
    }

    .movie-card img {
        border-radius: 10px;
        width: 200px;
        height: 200px;  /* Ukuran poster diperbesar */
        object-fit: cover;  /* Agar proporsi poster terjaga */
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    .movie-title {
        font-size: 18px;  /* Ukuran font diperbesar */
        font-weight: 700;
        color: #000;  
        margin-top: 10px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        font-family: 'Segoe UI', sans-serif;
    }

    section[data-testid="stHorizontalBlock"] {
        gap: 2rem !important;
    }

    /* Styling tombol */
    .stButton>button {
        color: #ffff !important;
        border: 4px solid #28a745 !important;
        font-weight: 700;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #28a745 !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)


# =================== Fungsi Poster ===================
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or not data.get('poster_path'):
            return "https://via.placeholder.com/500x750?text=No+Poster"

        return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error"

# =================== Fungsi Rekomendasi ===================
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)

    recommended_names = []
    recommended_posters = []

    for i in distances[1:6]:  # Top 5 rekomendasi
        movie_id = movies.iloc[i[0]].movie_id
        recommended_names.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_names, recommended_posters

# =================== UI ===================
st.markdown('<div class="title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)

selected_movie = st.selectbox("Select a movie you like", movies['title'].values)

if st.button("🎥 Show Recommendations"):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie)

    columns = st.columns(4)  # Lebarkan kolom jadi 4
    for col, name, poster in zip(columns, names, posters):
        with col:
            card_html = f"""
                <div class="movie-card" style="max-width: 300px";>
                    <img src="{poster}" alt="Poster" />
                    <div class="movie-title">{name}</div>
                </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
