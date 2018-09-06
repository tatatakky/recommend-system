def txt_getter():
    import os
    from mecab_wakati import wakati
    dire = []
    book_list = os.listdir('./data')
    print(book_list)
    for i in range(len(book_list)):
        if book_list[i][-4:] == '.txt':
            with open('./data/'+ book_list[i]) as f:
                dire.append(wakati(f.read()))
    return dire, book_list
