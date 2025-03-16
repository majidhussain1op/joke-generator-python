import streamlit as st
import random
import requests

# Function to fetch a random joke from an API
def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n{joke_data['punchline']}"
        else:
            return "Failed to fetch a joke! Try again."
    except requests.exceptions.RequestException:
        return "Error fetching joke! Check your internet connection."

# Streamlit UI
st.title("🤣 Random Joke Generator 🤣")

st.write("Click the button below to get a random joke!")

if st.button("Get a Joke 🎭"):
    joke = get_random_joke()
    st.success(joke)
