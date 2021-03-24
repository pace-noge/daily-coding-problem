"""
The basic idea is to represent repeated successive characters as a single count
character. for example the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".
"""


def encode(s):
    d = [[s[0]]]
    for i in range(1, len(s)):
        if s[i] in d[-1]:
            d[-1].append(s[i])
        else:
            d.append([s[i]])
    return "".join(f"{len(x)}{x[0]}" for x in d )

if __name__ == "__main__":
    print(encode("AAAABBBCCDAA"))

