import streamlit as st

st.title("Surfeyene")

# Set the background image from a URL
st.markdown("""
<style>
body {
    background-image: url("https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.surfer.com%2Fculture%2Frugged-raw-and-beautiful-canada-by-marcus-paladino-photos&ved=0CBUQjRxqGAoTCNDon7iM15EDFQAAAAAdAAAAABD1AQ&opi=89978449");
    background-size: cover;
    background-attachment: fixed; /* Optional: Keeps image fixed when scrolling */
}
</style>
""", unsafe_allow_html=True)

st.title("My App with Background Image")
st.write("Content goes here...")
