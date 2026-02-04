import nltk
from collections import Counter

# Language model (prior probabilities)
word_counts = {
    "the": 5000,
    "tea": 2000,
    "team": 1000,
    "ten": 200
}

# Total word count (for normalization)
total_count = sum(word_counts.values())

def edit_distance_prob(wrong_input, w):
    """
    Likelihood P(O|S):
    How likely word w becomes wrong_input
    """
    distance = nltk.edit_distance(w, wrong_input)
    if distance == 0:
        return 1.0
    return 1 / (10 ** distance)

def prior_probability(w):
    """
    Prior probability P(S):
    How common the word is
    """
    return word_counts.get(w, 0) / total_count

def suggested(wrong_input):
    candidates = list(word_counts.keys())
    correct_word = None
    high_prob = -1

    for w in candidates:
        likelihood = edit_distance_prob(wrong_input, w)
        prior = prior_probability(w)

        # Noisy channel formula
        result = likelihood * prior

        if result > high_prob:
            high_prob = result
            correct_word = w

    return correct_word


# Test input
wrong_input = "teama"
correction = suggested(wrong_input)

print("Corrected word:", correction)