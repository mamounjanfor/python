command = ""
started = False
stopped = True
while True:
          command = input("> ").lower()
          if (command == 'help'):
               print("""
Start - to start the car
Stop  - to stop the car
quit  - to exit the program
                    """)
          elif (command == 'start'):
              if started:
                  print("Car already started ...")
              else:
                   started = True
                   print("Car start to gooo....")

          elif (command == 'stop'):

              if started == True:
                  started = False
                  print("Car Stopped !")

              else:
                  print("Car already Stopped...!")

          elif (command == 'quit'):
               print("Program quiting....!")
               exit()
               break

          else:
               print("I do not undersatand this...")


#Cameron was here, testing a push

