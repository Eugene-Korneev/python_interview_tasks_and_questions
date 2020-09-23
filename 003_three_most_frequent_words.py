from collections import Counter


string = "abba com mother bill mother com abba dog abba mother com"
words = string.split()
combinations = zip(words, words[1:], words[2:])
result_dict = {}

for c, n in Counter(combinations).items():
    for res_c, res_n in result_dict.items():
        if set(res_c.split()) == set(c):
            result_dict[res_c] += n
            break
    else:
        result_dict[' '.join(c)] = n

max_combination = sorted([*result_dict.items()], key=lambda item: -item[1])[0]
print(max_combination)
