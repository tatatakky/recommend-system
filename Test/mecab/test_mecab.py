def wakati(text):
    import MeCab
    tagger = MeCab.Tagger("-O wakati")
    divide_text = tagger.parse(text).split()
    return divide_text

if __name__ == '__main__':
    text = "僕はTWICEが大好きだ。"
    print(wakati(text))

