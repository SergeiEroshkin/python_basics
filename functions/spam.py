SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free', 'offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', 'help', 'widow'}


def spam_indicator(text):
    """
    This function returns the spam indicator rounded to two decimals
    """
    spam_counter = 0
    unique_words = set(text.lower().split())
    for word in unique_words:
        if word in SPAM_WORDS:
            spam_counter += 1
        else:
            continue
    return round(float(spam_counter) / float(len(unique_words)), 2)


def classify(indicator):
    """
    This function prints the spam classification
    """
    spam_threshold = 0.10
    if indicator > spam_threshold:
        return 'This message is: SPAM'
    else:
        return 'This message is: HAM'


def get_input():
    """
    Get user input and return it
    """
    user_input = raw_input('Please enter your message: ')
    return user_input


def main():
    message = get_input()
    spam = spam_indicator(message)
    print 'SPAM indicator: %s' % spam
    print classify(spam)


if __name__ == '__main__':
    main()
