def starts_with_vowel(word):
    """
    :param word: User-provided word
    :return: True if the word starts with a vowel and False otherwise
    """
    vowel = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowel:
        return True
    else:
        return False


def encrypt(word):
    """
    :param word: Word to be encrypted
    :return: Encrypted word
    """
    if starts_with_vowel(word):
        word = word + 'tan'
    else:
        word = word[1:] + word[0] + 'est'
    return word


def decrypt(word):
    """
    :param word: Word to be decrypted
    :return: Original word or None if one or more words does not have specific format
    """
    vowel = ['a', 'e', 'i', 'o', 'u']
    if len(word) > 4:
        if word[0] in vowel and word.endswith('tan'):
            return word[:-3]
        elif word[-4] not in vowel and word.endswith('est'):
            return word[-4] + word[:-4]
        else:
            print 'Invalid message.'
            return None
    else:
        print 'Invalid message.'
        return None


def translate(text, mode):
    """
    :param text: User-entered text
    :param mode: Encrypt if 'E' entered and Decrypt if 'D'
    :return: Single string from list of reversed translated word
    """
    splitter_text = text.split()
    if mode == str('E'):
        result = map(encrypt, splitter_text)
    elif mode == str('D'):
        result = map(decrypt, splitter_text)
    if None in result:
        return None
    else:
        result.reverse()
        return ' '.join(result)


def choose_mode():
    """
    :return: Mode to be performed
    """
    while True:
        mode = raw_input('Please type E to encrypt or D to decrypt a message: ')
        if mode == 'E' or mode == 'D':
            return mode
        else:
            print 'Invalid choice'


def main():
    mode = choose_mode()
    message = raw_input('Please enter your message: ')
    result = translate(message, mode)
    if result is None:
        pass
    else:
        print 'The secret message is: ' + result


if __name__ == '__main__':
    main()



