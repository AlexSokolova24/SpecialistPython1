# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

a = float(input("Введите сторону треуголбника а:"))  
b = float(input("Введите сторону треуголбника b:"))  
c = float(input("Введите сторону треуголбника c:"))  

if a == b and a == c and b == c:
    print("YES")
else:    
    print("NO")
