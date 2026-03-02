def say(msg, count=1):
    for i in range(count):
        print(msg)

say("Hi")
say("Bye", 3)


def sum_list(arr):
    arr_value = 0
    for i in arr:
        arr_value = arr_value + i
    return arr_value

print(sum_list([1, 2, 3]))