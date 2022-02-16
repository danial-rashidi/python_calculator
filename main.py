import math

while True:

    #plus function
    def plus_1():
        number = []
        for i in range(1,1000):
            print("---------------------------")
            inp_1 = int(input("Number %i : "%(i)))
            number.append(int(inp_1))
            inp_2 = input("Do you want to add More? (y/n) : ")
            if inp_2 == "yes" or inp_2 == "Yes" or inp_2 == "y" or inp_2 == "YES" :
                continue
            else:
                break
        result = []
        for x in number:
            result.append(str(x))
            result.append(" + ")
        result.pop()
        total = sum(number)
        result.append(" = ")
        result.append(total)
        print("")
        print(*result, sep='')

    #minus function
    def minus_2():
        print("---------------------------")
        inp_1 = int(input("Number : "))
        print("")
        inp_2 = int(input("to Subtract : "))
        result = inp_1 - inp_2
        print("")
        print(inp_1,"-",inp_2," = ",result)

    #Multiply function
    def multiply_3():
        print("---------------------------")
        inp_1 = int(input("Number : "))
        print("")
        inp_2 = int(input("to Multiply : "))
        result = inp_1 * inp_2
        print("")
        print(inp_1,"x",inp_2," = ",result)

    #division function
    def division_4():
        print("---------------------------")
        inp_1 = int(input("Number : "))
        print("")
        inp_2 = int(input("to Divide : "))
        result = inp_1 / inp_2
        print("")
        print(inp_1,"÷",inp_2," = ",int(result))

    #exponent function
    def exponent_5():
        print("---------------------------")
        inp_1 = int(input("Number : "))
        print("")
        inp_2 = int(input("To power : "))
        print("")
        result = int(math.pow(inp_1,inp_2))
        print(inp_1,"^",inp_2," = ",result)

    #square root function
    def square_root_6():
        print("---------------------------")
        inp = int(input("Number : "))
        print("")
        result = int(math.sqrt(inp))
        print("√%s"%(inp),"=", result)

    print("")
    print("1 : Plus         +")
    print("2 : Minus        -")
    print("3 : Multiply     x")
    print("4 : Division     ÷")
    print("5 : Exponent     ^")
    print("6 : Square root  √")
    print("")

    #main input
    inp = int(input("Enter Your Choice (1-6) : "))

    #plus
    if inp == 1:
        plus_1()

    #minus
    elif inp == 2:
        minus_2()

    #multiply
    elif inp == 3:
        multiply_3()

    #division
    elif inp == 4:
        division_4()

    #exponent
    elif inp == 5:
        exponent_5()

    #square_root
    elif inp == 6:
        square_root_6()

    print("---------------------------")
    restart_inp = input("Restart Program? (y/n) :")
    if restart_inp == "yes" or restart_inp == "Yes" or restart_inp == "y" or restart_inp == "YES" :
        continue
    else:
        break
     
