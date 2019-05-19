# Q2
def common_elements(list1, list2):
    unique_l1 = set(list1)
    unique_l2 = set(list2)
    common = []
    for i in unique_l1:
        if i in unique_l2:
            common.append(i)
    common.sort()
    return common

print(common_elements([3,1,2],[2,4,3]))
print(common_elements([3,3,2],[3,3,4,5]) == [3])