# count of the repetation of the characters in the string


def count_characters(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)


print(count_characters("we always have a another chance to live a beautiful life"))
