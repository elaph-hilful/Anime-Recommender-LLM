import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

question = st.text_input("Please enter the type of Anime you prefer to watch eg: Believes in “never give up” energy and emotional ninja drama.") 

if question:
    with st.spinner("Fetching recommendations for you..."):
        response = pipeline.recommend(question)
        st.markdown('### Recommended Anime:')
        st.write(response)