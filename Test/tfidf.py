def calc_tfidf(sentence, sentence_all):
    from tf import calc_tf
    from idf import calc_idf
    tf, word_list = calc_tf(sentence)
    idf = calc_idf(sentence_all, word_list)
    import numpy as np
    tfidf = list(np.array(tf) * np.array(idf))
    return tfidf, word_list
