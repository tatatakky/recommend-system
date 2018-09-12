def calc_tf(data_for_tf):
    counter_of_words_t, name_of_words_t = [],[]
    data_for_tf_list = data_for_tf.split()
    sigma_sentence_count = len(data_for_tf_list)
    for i in range(sigma_sentence_count):
        if data_for_tf_list[i] not in name_of_words_t:
            name_of_words_t.append(data_for_tf_list[i])
            counter_of_words_t.append(1)
        else:
            counter_of_words_t[name_of_words_t.index(data_for_tf_list[i])] += 1
    return list(map(lambda x : x/sigma_sentence_count, counter_of_words_t)) , name_of_words_t
