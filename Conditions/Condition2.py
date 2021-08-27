'''If temperature is greater than 30, it's a hot day other wise if it's less than 10;
 it's a cold day; otherwise, it's neither hot nor cold.'''
temp = int(input("enter temperature :"))
if temp>=30:
    print('Its a hot day')
elif temp<=10:
    print('Its a cold day')
else:
    print(f'The Temperature is moderate')


