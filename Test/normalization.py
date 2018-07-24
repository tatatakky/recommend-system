def normalize(word_list_i, tfidf, word_for_normalization, list_for_normalization):
    #処理

    for i in range(len(word_list_i)):
        idx = word_for_normalization.index(word_list_i[i])
        idx_tfidf = word_list_i.index(word_list_i[i])
        list_for_normalization[idx] = tfidf[idx_tfidf]
    return list_for_normalization


# if __name__ == '__main__':
    # tfidf = [0.09197729088941291, 0.17044959722284933, 0.34089919444569866, 0.17044959722284933, 0.34089919444569866, 0.07142857142857142, 0.12093908432571038, 0.34089919444569866, 0.17044959722284933, 0.17044959722284933, 0.12093908432571038]
    # word_list_i = ['I', 'like', 'soccer', 'and', 'baseball', 'is', 'good', 'sports', 'basketball', 'volleyball', 'are']
    # word_for_normalization = ['today', 'is', 'sunny', 'weather', 'cloudy', 'snow', 'rainy', 'cloud', 'It', 'hot', 'I', 'like', 'soccer', 'and', 'baseball', 'good', 'sports', 'basketball', 'volleyball',
    # 'are', 'often', 'use', 'computer', 'A', 'a', 'device', 'Computers', 'used', 'as', 'control', 'systems', 'software', 'hardware', 'middleware', 'science', 'sky', 'man', 'great', 'rain',
    # 'cold']
    # list_for_normalization = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0]

    # normalize(word_list_i, tfidf, word_for_normalization,list_for_normalization)
