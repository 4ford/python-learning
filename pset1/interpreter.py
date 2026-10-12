import re

expression = input("Expression: ")
numbers = numbers = re.findall(r'\d+\.\d+|\d+', expression)
clean_numbers = [float(n) if '.' in n else int(n) for n in numbers]
x = clean_numbers[0]
z = clean_numbers[1]
y = expression.translate(str.maketrans('','','1234567890')).strip()

if y == '+':
    print(float((x + z)))
elif y == '-':
    print(float((x - z)))
elif y == '/':
    print(float((x/z)))
else:
    print(float((x * z)))

#Lesson Learned - I overcomplicated the code by using regex and translate. I could have just used split() to get the num.