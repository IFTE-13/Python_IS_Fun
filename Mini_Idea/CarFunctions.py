command = ""
start = False
while True:
    command = input('> ').lower()
    if(command == 'start'):
        if start:
            print('Hey! The car is already started.')
        else:
            start = True
            print('Car is started')
    elif(command == 'stop'):
        if not start:
            print('Bro, first start the car!')
        else:
            start = False
            print('the car is stopped')
    elif(command == 'help'):
        print("""
        Enter:
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print('Sorry, enter a valid command')