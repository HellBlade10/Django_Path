operation = int(input("Choose:\n"
"1 for add\n"
"2 for subtract\n"
"3 for multiply\n"
"4 for divide\n"
"=> "))
x = 0
sum = 0
difference = 0
product = 1
divide = 1
value = []
while x==False:
    if operation == 1:
        numbers = input("Add number? : ")
        if numbers == 'q':
            break
        else:
            numbers = int(numbers)
    
    # Letting a user see stored numbers inside a list or array.
            sum += numbers
    elif operation == 2:
        numbers = input("Add number? : ")
        if numbers == 'q':
            break
        else:
            numbers = int(numbers)
        difference -= numbers
    elif operation == 3:
        numbers = input("Add number? : ")
        if numbers == 'q':
            break
        else:
            numbers = int(numbers)
            product *= numbers
    elif operation == 4:
        numbers = input("Add number? : ")
        if numbers == 'q':
            break
        else:
            numbers = int(numbers)
            if numbers != 0:
                divide /= numbers
            else:
                print("Error: Division by zero is not allowed")
                break


if operation == 1:
    print("Sum is {}".format(sum))
elif operation == 2:
    print("Difference is {}".format(difference))
elif operation == 3:
    print("Product is {}".format(product))
elif operation == 4:
    print("Quotient is {}".format(divide))
else:
    print("Invalid operation")