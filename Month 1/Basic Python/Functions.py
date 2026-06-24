numbers = [1, 23, 3]

def demo(numbers):
    for i in numbers:
        print(i)

demo(numbers)


str1 = ["uday", "patil"]
ans = []

def print_list(list1: list[str], ans: list[str], str1: list[str]) -> list[str]:

    print(str1)

    for i in list1:
        ans.append(str(i))

    return ans

result = print_list(str1, ans, str1)

print("New List:", result)