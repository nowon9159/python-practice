person = {
    "name": "홍길동",
    "age": 20,
    "city": "서울"
}

print(person["name"])
print(person["age"])

person["email"] = "hong@example.com"

print(person)

print(person.get("name"))
print(person.get("phone"))
print(person.get("phone", "없음"))


if "city" in person:
    print(person["city"])

