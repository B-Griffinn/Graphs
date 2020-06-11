# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.


# nested for loop
# get min from each arr push that to a list
# sum every element in new arr


my_list = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
sum_list = []
numbers_sum = 0
for i in my_list:
    # print(i)
    numbers_sum += min(i)
    # lowest_num = None
    # for j in i:
    #     # print(j)
    #     if lowest_num is None:
    #         lowest_num = j
    #     if lowest_num > j:
    #         lowest_num = j
    # # print(lowest_num)
    # sum_list.append(lowest_num)

# sum all contents in sum_list
print(numbers_sum)
