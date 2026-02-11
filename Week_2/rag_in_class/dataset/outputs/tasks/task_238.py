def number_of_substrings(s):
    s_len = len(s)
    return int(s_len * (s_len + 1) / 2)
