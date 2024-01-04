import requests
from bs4 import BeautifulSoup

# Get the text from the link
url = "https://www.o-bible.com/download/kjv.txt"
response = requests.get(url)
content = response.text

# Split the content into verses
verses = content.split("\n")

# Define the synonyms for the words 'violence' and 'god'
violence_synonyms = ['force', 'aggressiveness', 'kill']
god_synonyms = ['deity', 'god', 'supreme being']

# Store the identified verses in a list
found_verses = []
for verse in verses:
    for violence in violence_synonyms:
        for god in god_synonyms:
            if violence in verse.lower() and god in verse.lower():
                found_verses.append(verse)
                break

# Save the found verses in a text file
with open("kjv_verses_violence_god.txt", "w") as file:
    for verse in found_verses:
        file.write(verse + "\n")

# Display the found verses on the screen
for verse in found_verses:
    print(verse)
