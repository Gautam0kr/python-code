print("Alternate alphabet in capital letter:")
ALBHABETS=[]
for i in range(0, 26, 2):
    ALBHABETS.append(chr(i+65))
for alphabet in ALBHABETS:
    print(alphabet)

print()
print("Alternate alphabet in small letter: ")
alphabets=[]
for i in range(0, 26, 2):
    alphabets.append(chr(97+i))
for alphabet in alphabets:
    print(alphabet)