def reverse(text):
    # create empty string to store reversed string in future
    reversed_text = ''
    # Lets get length of string and use it to call letters by index
    length = len(text) - 1
    while length >= 0:
        reversed_text += text[length]
        length -= 1
    return reversed_text


print reverse('hello')