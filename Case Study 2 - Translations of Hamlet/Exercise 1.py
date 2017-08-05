from collections import Counter

def word_count_distribution(text):
    word_count = count_words_fast(text)
    count_distribution = Counter(word_count.values())
    return count_distribution
    
distribution = word_count_distribution(text)