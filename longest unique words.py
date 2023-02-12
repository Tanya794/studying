def get_n_longest_unique_words(words, n):
    
    dict = {}
    new_words = []


    for w in words:
        x = words.count(w)
        dict[w] = x

    for item in dict:
        if dict[item] < 2:
            new_words.append(item)

    new_words.sort(reverse = True, key = len)

    my_words = new_words[:n]

    return my_words
