# Print out numbers using * to remove brackets:
# my_list = [1, 2, 3, 4, 5]
# print(my_list) ==> [1, 2, 3, 4, 5]
# print(*my_list) ==> 1, 2, 3, 4, 5

# Using Slicing:
# my_list = [1, 2, 3, 4, 5]
# print(*my_list[::-1])

# Using build-in function reversedDDDDD():
# my_list = [1, 2, 3, 4, 5]
# print(*list(reversed(my_list)))

# Using build-in method list.reverse():
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print(*my_list)

# Using build-in function sortedDDDD(list, reverse=True)
# my_list = [1, 2, 3, 4, 5]
# print(*sorted(my_list, reverse=True))

# Using build-in method sort(reverse=True)
# my_list = [1, 2, 3, 4, 5]
# my_list.sort(reverse=True)
# print(*my_list)

# Using for loop and string concatination:
# my_list = [1, 2, 3, 4, 5]
# reverse = ''
# for i in my_list:
#     reverse = str(i) + reverse
# print(*reverse)

# Using build-in functions join() & reverseDDDDD()
# my_list = [1, 2, 3, 4, 5]
# print(''.join(reversed(str(my_list))).replace(']', '').replace('[', ''))

# Using for loop and another list:
# my_list = [1, 2, 3, 4, 5]
# reverse = []
# for i in reversed(my_list):
#     reverse.append(i)
# print(*reverse)
# print('Using for loop and another list')

# Using while loop and another list:
# my_list = [1, 2, 3, 4, 5]
# reverse = []
# count = len(my_list)
# while count != 0:
#     reverse.append(my_list[count - 1])
#     count -= 1
# print(*reverse)
# print('Using while loop and another list')

# Using bitwise operator and for loop:
# my_list = [1, 2, 3, 4, 5]
# for i in range(0, len(my_list), 1):
#     print(my_list[~i], end=", ")
# print("\n Using bitwise operator '~' and for loop")

# Using bitwise complement operator:
# my_list = [1, 2, 3, 4, 5]
# print(*[my_list[~i]for i, x in enumerate(my_list)])

# Using list comprehension and for loop:
# my_list = [1, 2, 3, 4, 5]
# for i in range(len(my_list), 0, -1):
#     print(my_list[i - 1], end=", ")

# Using list comprehention:
# my_list = [1, 2, 3, 4, 5]
# print(*[my_list[i-1] for i in range(len(my_list), 0, -1)])

# Using lambda:
# from functools import reduce
# my_list = [1, 2, 3, 4, 5]
# print(*reduce(lambda a, b: [b] + a, my_list, []))
# print("Using lambda")

