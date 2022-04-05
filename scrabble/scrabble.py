def run_scrabble(word):
    '''Calculates permutations for any character combination between 2-6 letters.
    Accepts 2 wildcards '''

    # itertools is a python module that provides permutative functions.
    # score_word is a function deriving from locally-made wordscore module.
    
    import itertools 
    from wordscore import score_word 
    import operator
    total_list = []

    def lexicographical_permutation(str):
        candidate_words = []
        i = 2
        while i <= len(word):
            for x in sorted(''.join(chars) for chars in itertools.permutations(str,i)):
                candidate_words.append(x)
            i += 1
        return candidate_words

    # import a scrabble word txt file to reference python-generated words with scrabble words.
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]
    data = list(data)
    data_dict = {}
    i = 2
    while i <= len(word):
        sub_list = []
        for value in data:
            if len(value) == i:
                sub_list.append(value)
            else:
                pass
        data_dict[i] = sub_list
        i += 1
    # convert word to upercase and check that all input parameters are correct. Otherwise, return warning.
    word = word.upper()
    for letter in word:
        if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ?*":
            return f"Your word contains an invalid character"
    if len(word) < 2 or len(word) > 6:
        return f"Your word needs to be between 2 to 6 letters."
    if word.count("*") + word.count("?") > 2:
        return f"You can only have 2 wildcard characters."
    if word.count("*") > 1:
        return f"You must have less than 2 * characters for wildcard."
    if word.count("?") > 1:
        return f"You must have less than 2 ? characters for wildcard."
    
    # Create list of possible combinations and permuitations for word. 
    # If no wildcard, be more specific and include permutations. Otherwise, use combinations only.

    guess_list = []
    score_list = []

    wild = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    candidate_words = lexicographical_permutation(word)
    candidate_words = list(set(candidate_words))
    candidate_words.sort(reverse = True)

    for value in candidate_words:
        if "*" in value and "?" not in value:
            i = 0
            score = score_word(value)   
            while i < len(wild):
                guess = value.replace("*", wild[i])
                if guess in data_dict[len(guess)]:
                    guess_list.append(guess)
                    score_list.append(score)
                else:
                    pass
                i += 1
        elif "?" in value and "*" not in value:
            i = 0
            score = score_word(value)
            while i < len(wild):
                guess = value.replace("?", wild[i])
                if guess in data_dict[len(guess)]:
                    guess_list.append(guess)
                    score_list.append(score)
                else:
                    pass
                i += 1
        elif "?" in value and "*" in value:
            score = score_word(value)
            i = 0
            while i < len(wild):
                guess1 = value.replace("*", wild[i])
                j = 0
                while j < len(wild):
                    guess2 = guess1.replace("?", wild[j])
                    if guess2 in data_dict[len(guess2)]:
                        guess_list.append(guess2)
                        score_list.append(score)
                    else:
                        pass
                    j += 1
                i += 1
        elif "?" not in value and "*" not in value:
            score = score_word(value)
            if value in data_dict[len(value)]:
                guess_list.append(value)
                score_list.append(score)
            else:
                pass  

    real_guess_list = []
    real_score_list = []
    
    i = 0
    while i < len(guess_list):
        if guess_list[i] not in real_guess_list:
            real_guess_list.append(guess_list[i])
            real_score_list.append(score_list[i])
        i += 1

    i = 0
    while i < len(real_score_list):
        total_list.append(tuple((real_score_list[i], real_guess_list[i])))
        i += 1

    total_list.sort(reverse = True, key = operator.itemgetter(0,1))

    total_dictionary = {}
    for row in total_list: 
        if row[0] not in total_dictionary:
            total_dictionary[row[0]] = []
        total_dictionary[row[0]].append(row[1])
    
    final_list = []
    for scores in total_dictionary:
        total_dictionary[scores].sort()
        for words in total_dictionary[scores]:
            final_list.append(tuple((scores, words)))
    
    final_list = tuple((final_list, len(final_list)))

    return final_list