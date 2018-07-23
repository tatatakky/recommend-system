def normalize(tfidf, word_list_i, word_for_normalization, list_for_normalization):
    #処理
    return 0


if __name__ == '__main__':
    tfidf = [0.1302420908123035, 0.23076923076923078, 0.260484181624607, 0.1302420908123035, 0.1302420908123035, 0.1302420908123035, 0.1302420908123035, 0.1302420908123035, 0.18356110470153006, 0.1302420908123035]
    word_list_i = ['today', 'is', 'sunny', 'weather', 'cloudy', 'snow', 'rainy', 'cloud', 'It', 'hot']
    word_for_normalization = ['today', 'is', 'sunny', 'weather', 'cloudy', 'snow', 'rainy', 'cloud', 'It', 'hot', 'I', 'like', 'soccer', 'and', 'baseball', 'good', 'sports', 'basketball', 'volleyball',
    'are', 'often', 'use', 'computer', 'A', 'a', 'device', 'Computers', 'used', 'as', 'control', 'systems', 'software', 'hardware', 'middleware', 'science', 'sky', 'man', 'great', 'rain',
    'cold']
    list_for_normalization = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0]

    normalize(tfidf, word_list_i, word_for_normalization,list_for_normalization)
