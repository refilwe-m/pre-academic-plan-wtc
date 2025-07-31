while True:
    try:
        fuel = input("Fraction: ")
        [x,y] = fuel.split("/")
        if int(y)<int(x) or int(y)<0 or int(x)<0:
            raise 
        percentage = round((int(x)/int(y))*100)
        result = 'E' if percentage<=1 else 'F' if percentage >=99 else f"{percentage}%"
        print(result)
        break
    except:
         fuel = input("Fraction: ")