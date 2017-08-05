import string
alphabet = string.ascii_letters

def counter(sentence):
    count_letters = {}
    for i in sentence:
        if i in alphabet:
            count_letters[i] = sentence.count(i)
    return count_letters;
    
sentence = 'Jim quickly realized that the beautiful gowns are expensive'
count_letter = counter(sentence)