def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str):
    s_length = len(s)
    if not s[:2].isalpha() or not s.isalnum() or s_length >6 or s_length<2:
        return False
    
    has_num = False
    for char in s:
        if char.isdigit():
            if char =='0' and not has_num:
                return False
            else: 
                has_num = True
        elif char.isalpha() and has_num:
            return False
    
    return True


main()