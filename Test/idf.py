def calc_idf(data_for_idf, words_list):
    import numpy as np
    count_sentence_in_words_list = []
    N = len(data_for_idf)
    for i in range(len(words_list)):
        count = 0
        for j in range(N):
            if words_list[i] in data_for_idf[j]:
                count += 1
        count_sentence_in_words_list.append(N/count)
    return list(map(lambda x : x+1, list(np.log(count_sentence_in_words_list))))
