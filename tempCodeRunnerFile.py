def validate_float(input_str):
    if len(input_str)==1:
        return False
    try:
        float_value = float(input_str)
        return True
    except ValueError:
        return False
n=int(input())
for _ in range(n):
    
    user_input = input()
    if validate_float(user_input):
        print("True")
    else:
        print("False")
