print("Hello, This program to convert from Kg-lbs Or Lbs-Kg")
val1 = input("please select your option \n [1] convert from kg-to-LBS\n [2] for LBS-to-Kg\n [q] to exit \n")


while True:

  try:

    if val1 == 'q' or val1 == 'Q':
           print("Thanks you,closing the program...")
           exit()

    elif val1 == '1':
             try:
                   kg = float(input("Kilogram value that you want to convert to LBS: "))
                   lbs = float(kg * 2.205)
                   print('The value of {} Kg, is equl to {} lbs'.format(kg, lbs))
                   break
             except ValueError:
                 print("That's not an numeric!")

    elif val1 == '2':
            try:
                    lbs = float(input("LBS value that you want to convert to Kg: "))
                    kg =  float( lbs * 0.4535)
                    print('The value of %.2f lbs, is equl to %.2f kg' % (lbs, kg))
                    break
            except ValueError:
                    print("That's not an numeric!")

    else:
        print("Unknown value...")
        exit()
        break


  except ValueError:
      print("Non.....")