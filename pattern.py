#rows = int(input("Enter number of rows: "))
print("select pattern")
print("1.half pyramid")
print("2. inverted half pyramid")
print("3. Full Pyramid")

rows = 4
while True:
    # take input from the user
    choice = input("Enter choice(1/2/3): ")

    if choice in ('1', '2', '3'):
        if choice == '1':
            for i in range(rows):
               for j in range(i+1):
                   print("* ", end="")
               print("\n")


        elif choice == '2':
           for i in range(rows, 0, -1):
              for j in range(0, i):
                  print("* ", end=" ")
              print("\n")



        elif choice == '3':
           k = 0
           for i in range(1, rows + 1):
              for space in range(1, (rows - i) + 1):
                  print(end="  ")

              while k != (2 * i - 1):
                  print("* ", end="")
                  k += 1

              k = 0
              print()



        next_calculation = input("Do you want to see the pattern again? (yes/no): ")
        if next_calculation == "no":
            break