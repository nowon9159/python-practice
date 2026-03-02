score = 95

if score >= 70:
    print("합격")
else:
    print("불합격")

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("입장 가능")
    print(type(has_ticket))