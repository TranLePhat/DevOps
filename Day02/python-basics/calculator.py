a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))

tong = a + b
hieu = a - b
tich = a * b
thuong = a / b

tong1 = a + c
tich1 = a * b * c
thuong = a / c


print(f"Tong a va b: {tong}")
print(f"Hieu a va b: {hieu}")
print(f"Tich a va b: {tich}")
print(f"Thuong a va b: {thuong}")

print(f"Tong a va c: {tong1}")
print(f"Tich a va b va c: {tich1}")
print(f"Thuong a va c: {thuong}")