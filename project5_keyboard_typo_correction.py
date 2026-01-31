def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )

    return dp[m][n]


def weighted_keyboard_distance(word1, word2):
    # Keyboard adjacency (simplified)
    keyboard_neighbors = {
        'o': ['p'],
        'p': ['o']
    }

    cost = 0
    for c1, c2 in zip(word1, word2):
        if c1 == c2:
            continue
        elif c2 in keyboard_neighbors.get(c1, []):
            cost += 0.5   # nearby key
        else:
            cost += 1     # normal mistake

    cost += abs(len(word1) - len(word2))
    return cost


typed_word = "HELLP"
correct_word = "HELLO"

standard_distance = levenshtein_distance(typed_word, correct_word)
weighted_distance = weighted_keyboard_distance(typed_word, correct_word)

print("Standard Levenshtein Distance:", standard_distance)
print("Weighted Keyboard Distance:", weighted_distance)

if weighted_distance < standard_distance:
    print("Suggested correction: HELLO")
else:
    print("Correction uncertain")
