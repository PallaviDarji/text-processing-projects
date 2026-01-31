import re

def clean_for_sentiment(text):
    # convert to lowercase
    text = text.lower()

    # remove hashtags
    text = re.sub(r'#\w+', '', text)

    # remove punctuation and special characters
    text = re.sub(r'[^a-z\s]', '', text)

    # split into words
    words = text.split()

    # common stopwords
    stop_words = {"this", "the", "it", "but", "were"}

    cleaned_words = []

    for word in words:
        if word not in stop_words:
            cleaned_words.append(word)

    return cleaned_words


input_a = "I Love this movie!!! #awesome #friday"
input_b = "I Love this movie ,but the seats were bad"
input_c = "Loved it! Best.Moive.Ever"

print("A:", clean_for_sentiment(input_a))
print("B:", clean_for_sentiment(input_b))
print("C:", clean_for_sentiment(input_c))
