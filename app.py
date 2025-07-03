import streamlit as st
from recommender import get_hybrid_recommendations

st.title("🎬 Smart Movie Recommendation Engine")

movie = st.text_input("Enter a movie title:")
if movie:
    results = get_hybrid_recommendations(movie)
    st.subheader("Recommended Movies:")
    for r in results:
        st.write(f"- {r}")
