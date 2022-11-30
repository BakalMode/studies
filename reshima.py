import re

def func1(file):

    word_len = 0
    len_count_dict = {}
    for sentence in file:
        for letter in sentence:

            regex_res = re.search("[a-z]|[A-Z]", letter)
            if regex_res != None:
                word_len+=1
            elif word_len != 0:
                if word_len in len_count_dict:
                    len_count_dict[word_len] += 1
                else:
                    len_count_dict[word_len] = 1
                word_len = 0
    return len_count_dict

file = "C:\\Users\\turht\\Desktop\\haciendo.txt"
with open(file, "r") as f:
  answer = func1(f)
  print(answer)


