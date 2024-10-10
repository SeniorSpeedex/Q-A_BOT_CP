from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def obama_func(base, base1):
    vector = TfidfVectorizer()
    matric = vector.fit_transform([base, base1])
    cosinus_reg = cosine_similarity(matric[0:1], matric[1:2])

    return cosinus_reg[0][0] * 100

# Результат
reco_txt = obama_func('Ты и я', 'Я и ты')