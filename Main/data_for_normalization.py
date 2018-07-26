def make_normalization_data(data):
    word = ""
    for i in range(len(data)):
        word += data[i] + " "
    l = word.split()
    word_for_normalization = sorted(set(l), key=l.index)
    list_for_normalization = [0 for i in range(len(word_for_normalization))]
    return word_for_normalization , list_for_normalization
