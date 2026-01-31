import re

def clean_sentence(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-z\s]', '', sentence)

    words = sentence.split()

    stop_words = {"the", "are", "there", "over"}

    cleaned_words = []

    for word in words:
        if word not in stop_words:
            if word.endswith("es"):
                word = word[:-2]
            elif word.endswith("s"):
                word = word[:-1]
            elif word.endswith("ing"):
                word = word[:-3]

            cleaned_words.append(word)

    return cleaned_words


text = "The quick BROWN foxes... there are JUMPING over 10 lazy dogs!"
result = clean_sentence(text)

print(result)
