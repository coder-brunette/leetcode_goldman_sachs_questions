def check_string_and_word_from_dict(d, str):
    longest_word = ""
    str_lst = list(str)

    def can_form_word(word, letters):
        word_count = {}
        for letter in word:
            word_count[letter] = word_count.get(letter, 0) + 1
        for letter in word_count:
            if letter not in letters and word_count[letter] > letters.count(letter):
                return False
        return True

    for word in d:
        if can_form_word(word, str_lst) and len(word) > len(longest_word):
            longest_word = word
    return longest_word


print(check_string_and_word_from_dict({"to", "banana", "toe", "dogs", "ababcd", "elephant"}, "eot"))