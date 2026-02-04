import math

# low perplexity --> good model
# high perplexity --> bad/confused model

probabilities = [0.9, 0.8, 0.95]

def cal_perplexity(prob):
    entropy = -sum(math.log2(p) for p in prob) / len(prob)
    return 2 ** entropy

result = cal_perplexity(probabilities)
print(result)
