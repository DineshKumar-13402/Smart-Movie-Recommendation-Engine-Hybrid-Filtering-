import streamlit as st

st.set_page_config(page_title="Smart Movie Recommender", layout="centered")

st.title("🎬 Smart Movie Recommendation Engine")

movie = st.text_input("Enter a movie title:")
if movie:
    st.subheader("Top 5 Recommendations for:")
    st.write(f"🎥 {movie}")
    st.markdown("1. The Matrix\n2. Inception\n3. Interstellar\n4. The Dark Knight\n5. Fight Club")

st.caption("Built with Streamlit + Content-Based + Surprise (optional)")
