from gtts import gTTS

# Text to convert to speech
text = "wicket"

# Language for the speech
language = 'en'

# Convert text to speech
tts = gTTS(text=text, lang=language, slow=False)

# Save the audio as an MP3 file
tts.save("out.mp3")

print("Audio file saved as output.mp3")
