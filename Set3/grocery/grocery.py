grocery_list = []

while True:
    try:
        user_input = input().lower().strip()
        if user_input == "":
            break
        grocery_list.append(user_input)
    except EOFError:
        break
    
for item in sorted(set(grocery_list)):
    print(f"{grocery_list.count(item)} {item.upper()}",end="\n")
            
    