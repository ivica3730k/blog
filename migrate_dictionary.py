import json

# Open the JSON file
with open('cspell.json') as f:
    data = json.load(f)

# Extract the contents of the "words" key
words = data['words']

# Open the text file in append mode
with open('.custom-dictionary.txt', 'w') as f:
    # Write each word to the text file
    for word in words:
        f.write(word + '\n')
