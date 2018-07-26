def txt_getter():
    import os
    from mecab_wakati import wakati
    dire = []
    directory = os.listdir('./data')
    print(directory)
    for i in range(len(directory)):
        if directory[i][-4:] == '.txt':
            with open('./data/'+directory[i]) as f:
                dire.append(wakati(f.read()))
    return dire
