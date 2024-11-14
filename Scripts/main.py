while True:
    print('Hello!')
    string = input('Enter what to calculate: ')
    if string == 'q':
        break
    print(eval(string))
