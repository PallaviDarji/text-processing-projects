import re
def clean_for_sentiment(text):
    text = text.lower()
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
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

