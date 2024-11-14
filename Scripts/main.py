import datetime
print(datetime.datetime)
print('! Hello!')
while True:
    string = input('> Enter what to calculate: ').strip().lower()
    if string == 'q':
        print('! Bye!')
        break
    try:
        print(eval(string))
    except Exception as ex:
        print(f'! ERROR {ex}')
