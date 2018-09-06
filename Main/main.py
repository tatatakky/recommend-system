from tfidf import calc_tfidf
from make_data_japanese import make_jp_data
from data_for_normalization import make_normalization_data
from normalization import normalize
from cosine_similarity import calc_cosine_similarity
import numpy as np
from recommendation import recommend
def main():
    dic = {}
    normalization = []
    data, book_list = make_jp_data()
    for i in range(len(data)):
        tfidf, word_list_i = calc_tfidf(data[i], data)
        word_for_normalization, list_for_normalization = make_normalization_data(data)
        normalization.append(normalize(word_list_i, tfidf, word_for_normalization,list_for_normalization))

    print("\n\n===============similarity===============")
    similarity = calc_cosine_similarity(normalization)
    print(similarity)

    print("\n\n===============recommendation================")
    recommendation = recommend(similarity, book_list)
    for i, v in enumerate(recommendation.values()):
        print(i+1, v)

if __name__ == '__main__':
    main()
