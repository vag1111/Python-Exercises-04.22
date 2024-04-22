from googletrans import Translator
# This line has the phrase that I want translated
inserted_text = "Python is so powerful" 
translator = Translator() # Creates a translator object

# Attempt to translate whichever language you chose
translated_text = translator.translate(inserted_text, dest='pt').text
# Print the translated language
print(translated_text)
