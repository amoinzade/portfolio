# 1: Set the base score to 0. Import all scrabble letter scores as a dictionary.
# 2: For each letter in the input word, add the letter score value to the total score.
# 3: Return the net score.

def score_word(word):
    '''Imports scrabble scoring dictionary and assigns a score to each letter.'''
    score = 0
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10, "?": 0, "*": 0}
    for letter in word.lower():
        if letter in scores:
            score += scores[letter]
        else:
            pass
    return score