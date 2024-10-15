def reverse_words(s):
    s = s.split()
    reverse = s[::-1]
    result = ' '.join(reverse)
    print(result)

reverse_words("hello world!"), "world! hello"