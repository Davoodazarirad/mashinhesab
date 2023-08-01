x = input("Lotfan Adade aval ra vared konid: ")

y = input("Lotfan Adade dovom ra vared konid: ")

print("Amaliyate morede nazar ra entekhab namayed")

z = input("+ or - or * or / : ")

if z == "+":
    Jam = int(x) + int(y)
    print("Jam = ", Jam)
elif z == "-":
    Tafrigh = int(x) - int(y)
    print("Tafrigh = ", Tafrigh)
elif z == "*":
    Zarb = int(x) * int(y)
    print("Zarb = ", Zarb)
elif z == "/":
    Taghsim = int(x) / int(y)
    print("Taghsim = ", Taghsim)