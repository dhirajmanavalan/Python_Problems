password  = input("password: ")

has_digit = False
has_caps = False

for i in password:
    if i>='0' and i<='9':
        has_digit = True

    if i>="A" and i<="Z":
        has_caps = True

if has_caps and has_digit and len(password)>=8:

    print("Strong")
else:
    print("Weak")


