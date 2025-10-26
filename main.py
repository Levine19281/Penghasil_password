import random

kata = ""
tanya = int(input("berapa banyak kata yang diperlukan sebagai kata sandi: "))
for i in range(tanya):
    daftar = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+[]{}\|;:'?><.,"
    kata += random.choice(daftar)

print(kata) 