from tfidf import calc_tfidf
from make_data import data_maker
from data_for_normalization import make_normalization_data
from normalization import normalize
def main():
    data = data_maker()

    for i in range(len(data)):
        tfidf, word_list_i = calc_tfidf(data[i], data)
        word_for_normalization, list_for_normalization = make_normalization_data(data)
        print(normalize(word_list_i, tfidf, word_for_normalization,list_for_normalization))

if __name__ == '__main__':
    main()
