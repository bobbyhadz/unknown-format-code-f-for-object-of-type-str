# Unknown format code 'f' for object of type 'str'

my_float = '123.456789'

result = f'{float(my_float):.0f}'
print(result)  # 👉️ 123

result = f'The number is: {float(my_float):.0f}'
print(result)  # 👉️ The number is: 123