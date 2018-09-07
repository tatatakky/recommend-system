def txt_getter(bunsho_file):
    import os
    from mecab_wakati import wakati
    dire = []

    cmd1 = 'mv ' + bunsho_file + ' new.txt'
    os.system(cmd1)

    cmd2 = 'mv new.txt ./data'
    os.system(cmd2)

    book_list = os.listdir('./data')

    idx = book_list.index('new.txt')

    book_list[0], book_list[idx] = book_list[idx], book_list[0]

    #print(idx)


    print(book_list)
    for i in range(len(book_list)):
        if book_list[i][-4:] == '.txt':
            with open('./data/'+ book_list[i]) as f:
                dire.append(wakati(f.read()))
    return dire, book_list
