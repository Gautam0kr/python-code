name=str(input("Enter your name: "))
print(f"Your name is {name}")
temp=str(input("Enter first three char to change i name: "))
newName=temp+name[3:]
name=newName
print(name)
    