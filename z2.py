# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите x')
x = int(input())
print('Введите y')
y = int(input())
print('Введите z')
z = int(input())

left = not (x or y or z)
right = not x and not y and not z

if left == right:
    print('истина')
else:
    print('ложь')