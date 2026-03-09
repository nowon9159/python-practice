text = "name=홍길동,age=20"

split_text = text.strip().split(",")
split_text_text1 = split_text[0]
split_text_text2 = split_text[1]

print(split_text_text1)
print(split_text_text2)

split_name = split_text_text1.split("=")
split_age = split_text_text2.split("=")

print(split_name)
print(split_age)

dict_name_age = {
    split_name[0]: split_name[1],
    split_age[0]: split_age[1]
}

print(dict_name_age)


def key_return(some_dict):
    key_count = 0
    for i in some_dict:
        key_count += 1
    return key_count

print(key_return(dict_name_age))

fruits = "사과,바나나,포도"

def list_count_return(some_str):
    split_some_str = some_str.strip().split(",")
    return len(split_some_str)

print(list_count_return(fruits))