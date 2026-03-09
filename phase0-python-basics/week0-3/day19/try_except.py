nums = [1, 2, 3]

# print(nums[10])

try:
    print(nums[10])
except IndexError:
    print("인덱스 범위를 벗어났습니다.")

d = {"a": 1}

try:
    print(d["b"])
except KeyError:
    print("키가 없습니다")


int_error = int("abc")
print(int_error)