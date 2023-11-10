from gtts import gTTS

# Open the text file (book.txt)
file = open("book.txt", encoding="utf-8")
text = file.read()

language = 'en'

# Create a gTTS object with text and language, speed parameters and then save the audio file.
obj = gTTS(text=text, lang=language, slow=False)
obj.save("book.mp3")
file.close()