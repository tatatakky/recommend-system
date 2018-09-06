def recommend(similarity, book_list):
    dic = {}
    for x in range(len(similarity)):
        if similarity[x] >= float(0.8):
            dic[similarity[x]] = book_list[x]
        else:
            pass

    sorted( dic.items(), key = lambda x:x[0])

    return dic
