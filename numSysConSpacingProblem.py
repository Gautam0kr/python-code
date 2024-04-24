def print_formatted(number):
    n=str(number)
    s1=len(n)
    s2=len(oct(number)[2:])
    s3=len(hex(number)[2:])
    s4=len(bin(number)[2:])
    s5=s4-s1
    s6=s4-s2
    s7=s4-s3
    for num in range(1, number+1):
        print(" "*s5, end="")
        print(str(num).rjust(s1, " "), end=" ")
        print(" "*s6, end="")
        print(oct(num)[2:].rjust(s2, " "), end=" ")
        print(" "*s7, end="")
        print(hex(num)[2:].upper().rjust(s3, " "), end=" ")
        print(bin(num)[2:].rjust(s4, " "))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)