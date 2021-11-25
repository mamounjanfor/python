print("Hello, Which operation you need to do?")


val1 = input("Select from below options \n [1] for celsius-to-fahrenheit\n [2] for fahrenheit-to-celsius\n [q] to exit \n")


if val1 == 'q' or val1 == 'Q':
    print("Thank you, exit the program... ")
    exit()

if int(val1) == 1:
    celsius = float(input("Temperature value in degree Celsius: " ))
    Fahrenheit = (celsius * 1.8) + 32
    print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'
          % (celsius, Fahrenheit))

elif int(val1) == 2:
    Fahrenheit_1 = float(input("Temperature value in degree Fahrenheit: "))
    Celsius_1 = (Fahrenheit_1 - 32) * 5.0 / 9.0
    print('The %.2f degree Fahrenheit is equal to: %.2f Celsius'
          % (Fahrenheit_1,Celsius_1 ))







