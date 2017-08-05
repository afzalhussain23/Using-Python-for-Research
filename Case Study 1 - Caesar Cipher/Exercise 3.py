message = "hi my name is caesar"
def caesar(message, encryption_key):
    encoding = {alphabet[i] : (i + encryption_key) % 27 for i in range(27)}
    string = ""
    for i in range(len(message)):
        value = encoding[message[i]]
        string += letters[value]
    return string
    
encoded_message = caesar(message, encryption_key = 3)
print(encoded_message)