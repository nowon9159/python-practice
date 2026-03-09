# option A

dict_log = {}

with open("phase0-python-basics/week0-3/day20/app.txt") as f:
    for line in f:
        line = line.strip()
        dict_log[line] = dict_log.get(line, 0) + 1
    print(dict_log)
    max_word = ""
    max_value = 0
    for word in dict_log:
        if dict_log[word] > max_value:
            max_value = dict_log[word]
            max_word = word
    print(max_word)
            


# option B
# file 열어서 모든 라인 for 문으로 확인 하고, if문으로 ERROR 필터링하고 만들어둔 error list 에 넣어서 길이 출력하면 될거라고 생각함.
# error_list = []
# with open("app.log") as f:
#     for line in f:
#         if "[ERROR]" in line.strip():
#             error_list.append(line.strip())
#     print(len(error_list))

# option C
# 합계는 그냥 구하면 되고 평균은 합계에서 합계의 리스트 길이 구해서 나누면 됨
# 근데 평균을 int 형으로 출력할지 float으로 출력할지는 고민을 해봐야할듯? 아니면 인자값 하나 더 받아서 해도 될듯

# int_list = [1, 2, 3, 4, 5]

# def return_int_sum_avg(some_list):
#     int_sum_dict = {}
#     int_avg = 0
#     int_sum = 0

#     for i in some_list:
#         int_sum = int_sum + i
#     int_avg = int_sum / len(some_list)
#     int_sum_dict["int_sum"] = int_sum
#     int_sum_dict["int_avg"] = int_avg
#     return int_sum_dict

# print(return_int_sum_avg(int_list))

