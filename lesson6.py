import string

dict_1 = {k: v for k, v in
          zip([random.choice(string.ascii_lowercase) for _ in range(10)],
              [random.randint(1, 100) for _ in range(10)])}

dict_2 = {k: v for k, v in
          zip([random.choice(string.ascii_lowercase) for _ in range(10)],
              [random.randint(1, 100) for _ in range(10)])}

dict_3 = dict_1 | dict_2

print(dict_1)
print(dict_2)
for k, v in dict_3.items():
    if k in dict_1.keys():
        v = dict_1[k] if v < dict_3[k] else v
    dict_3[k] = v

print(dict_3)