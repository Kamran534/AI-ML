million = 1_000_0000
billion = 1_000_000_000

print(f"One million is written as: {million}")
print(f"One billion is written as: {billion}")

speed_of_light_mps = 3e8  # meters per second  --> 3x10^8
avogadro_number = 6.022e23  # particles per mole --> 6.022x10^23

print(f"Speed of light: {speed_of_light_mps} m/s")
print(f"Avogadro's number: {avogadro_number} particles/mole")

a = 10
b = 3

#  Division (always returns float)
division = a / b
print(f"{a} / {b} = {division}")  # 10 / 3 = 3.3333...

# Floor Division (rounds down to nearest integer)
floor_div = a // b
print(f"{a} // {b} = {floor_div}")  # 10 // 3 = 3

# Modulus (returns the remainder)
b = 20
modulus = a % b
print(f"{a} % {b} = {modulus}")  # 10 % 3 = 1

x = 10
print(f"Final value of x: {x}")
# These two are equivalent:
x = x + 5
print(f"Final value of x: {x}")
x += 5      # Shorthand
print(f"Final value of x: {x}")
# All arithmetic operators have shorthand versions:
x += 5      # x = x + 5
print(f"Final value of x: {x}")
x -= 3      # x = x - 3
print(f"Final value of x: {x}")
x *= 2      # x = x * 2
print(f"Final value of x: {x}")
x /= 4      # x = x / 4
print(f"Final value of x: {x}")
x //= 2     # x = x // 2
print(f"Final value of x: {x}")
x %= 3      # x = x % 3
print(f"Final value of x: {x}")
x **= 2     # x = x ** 2
print(f"Final value of x: {x}")

name = 'kamran'
_name = name[::-1]
print(_name)  # narmak
print(name)   # kamran
print(name * 3)  # kamrankamrankamran  
print(name.title())  # Kamran
print(name.title().upper().istitle())  # False

path = r"C:\Users\Name\Documents"
print(path)  # C:\Users\Name\Documents


text = "123"
print(f"Original: {text*2}")
if text.isdigit():
    number = int(text)
    print(f"Converted: {number*2}")
else:
    print("Cannot convert to integer")