def normalize(word_list_i, tfidf, word_for_normalization, list_for_normalization):
    for i in range(len(word_list_i)):
        idx = word_for_normalization.index(word_list_i[i])
        idx_tfidf = word_list_i.index(word_list_i[i])
        list_for_normalization[idx] = tfidf[idx_tfidf]
    print("---------normalized---------\n{}\n".format(list_for_normalization))
    return list_for_normalization
