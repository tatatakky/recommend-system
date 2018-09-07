def recommend(similarity, book_list):
    from collections import OrderedDict
    dic = {}
    for x in range(len(similarity)):
        if similarity[x] >= float(0.8):
            dic[similarity[x]] = book_list[x+1]
        else:
            pass
    return dic

