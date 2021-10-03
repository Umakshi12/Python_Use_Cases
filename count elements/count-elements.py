from collections import Counter

list1 = ['python', 'java', 'javascript', 'python', 'java', 'python']
list2 = ['python', 'java']
ans = Counter(list1)

print("Count of all elements in list1 ---")
print(ans)
print()

print("Count of elements of list1 which are present in list2 ---")
for i in range(len(list2)):
    print(list2[i], ans[list2[i]], sep=": ")
