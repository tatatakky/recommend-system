def wakati(text):
    import MeCab
    tagger = MeCab.Tagger("-O wakati")
    divide_text = tagger.parse(text).split()
    divided_sentence = ""
    for i in range(len(divide_text)):
        divided_sentence += divide_text[i] + " "
    return divided_sentence
