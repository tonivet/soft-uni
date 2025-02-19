start_char = input()
end_char = input()

def range_chars(fst, lst):
    char_str = ''
    for x in range(ord(fst)+1, ord(lst), 1):
        char_str += chr(x) + " "

    print(char_str)

range_chars(start_char, end_char)
