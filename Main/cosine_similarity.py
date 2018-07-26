def calc_cosine_similarity(normalization):
    import numpy as np
    similarity_data = []
    for i in range(1,len(normalization)):
        a,b = np.array(normalization[0]),np.array(normalization[i])
        similarity_data.append(np.dot(a,b)/(np.linalg.norm(a) * np.linalg.norm(b)))
    return similarity_data
