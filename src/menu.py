import auth
isRunning = True
def start():
    global isRunning
    while isRunning:
        print( """
        1.Authenticate user
        2.Register user
        3.Exit

        """)
        userInput = input("Select a number option: ")

        if userInput == "1":
            auth.authenticate() 
        elif userInput == "2":
            auth.register()
        elif userInput == "3":
            isRunning = False
            print("System shutdown")
        else:
            print("Invalid input")
            
            





