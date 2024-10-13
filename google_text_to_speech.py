import streamlit as st
from gtts import gTTS
import os

# Streamlit app layout
st.title("Text to Speech Converter")
st.write("Enter the text you want to convert to speech:")

# Input text
input_text = st.text_area("Enter text here","")



# Button to trigger text-to-speech conversion
if st.button("Convert to Speech"):
    if input_text:
        # Convert text to speech
        tts = gTTS(text=input_text, slow=False)
        
        # Save the audio file
        tts.save("output.mp3")
        
        # Play the audio file in the Streamlit app
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()

        # Streamlit audio player
        st.audio(audio_bytes, format="audio/mp3")
        st.success("Conversion successful!")
    else:
        st.error("Please enter some text.")

#Option to download the audio file
#if os.path.exists("output.mp3"):
    #with open("output.mp3", "rb") as audio_file:
        #st.download_button("Download Audio", audio_file, file_name="output.mp3")
st.write("This is the app for converting text to speech")