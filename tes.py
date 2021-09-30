def count_substring(txt, pat):
    a = 0
    b = None
    lis = []
    while a != b:
        b = a
        c = a
        if a == 0:
            a = txt.find(pat, a, len(txt))
            if a == -1:
                break
            lis.append(a)
        a = txt.find(pat, c + 1, len(txt))
        if a == -1:
            b == -1
            break
        lis.append(a)

    if len(lis) > 1:
        if lis[0] != 0:
            del lis[0]

    return len(lis)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)