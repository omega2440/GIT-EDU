while True:
    print('Hello!')
    string = input('Enter what to calculate: ')
    if string == 'quit':
        break
    print(eval(string))
