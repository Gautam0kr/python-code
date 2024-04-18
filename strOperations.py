if __name__ == '__main__':
    s = input()
    for ch in s:
        if ch.isalnum():
            print("True")
            break
    for ch in s:
        if ch.isalpha():
            print("True")
            break
    for ch in s:
        if ch.isdigit():
            print("True")
            break
    for ch in s:
        if ch.islower():
            print("True")
            break
    for ch in s:
        if ch.isupper():
            print("True")
            break
    else:
            print("False")
     