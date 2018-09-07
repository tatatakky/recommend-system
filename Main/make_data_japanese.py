def make_jp_data(bunsho_file):
    from get_txt import txt_getter
    li_data_txt, book_list = txt_getter(bunsho_file)
    return li_data_txt, book_list
