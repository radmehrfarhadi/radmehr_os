def Tools():
    print("1. 🧮Calculator")
    print("2. exit")
    whats_ = int(input("choose! choose!!"))
    if whats_ == 1:
        def c():
            inputs = input("your: ").strip()
            try:
                x, y, z = inputs.split(" ")
                y = str(y)
                x = int(x)
                z = int(z)
            except ValueError:
                print("Invalid! Example: 10 + 5")
                c()
                return
        
        
            if y == "+":
                anser = x + z

            elif y == "-":
                anser = x - z

            elif y == "*":
                anser = x * z

            elif y == "/":
                anser = x / z

            print(f"{anser}")

        c()
            
        
    elif whats_ == 2:
        return