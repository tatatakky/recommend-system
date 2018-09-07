def calc_tfidf(sentence, sentence_all):
    from tf import calc_tf
    from idf import calc_idf

    tf, word_list = calc_tf(sentence)
    #print("----------tf----------\n{}".format(tf))

    idf = calc_idf(sentence_all, word_list)
    #print("----------idf----------\n{}".format(idf))

    import numpy as np
    tfidf = list(np.array(tf) * np.array(idf))
    return tfidf, word_list
