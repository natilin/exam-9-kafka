def find_suspicious_words(sentences: list, suspicious_words: list):
    for sentence in sentences:
        for word in sentence.lower().split():
            if any(search_word in word for search_word in suspicious_words):
                return word
    return ""