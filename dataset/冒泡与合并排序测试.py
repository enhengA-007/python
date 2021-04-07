import time


def OpenFile(Str):  # 读取测试所用的数据
    with open(Str, 'r') as D:
        L = []
        line = D.readline()  # 读取文件中的数据数目
        length2 = lengeh = int(line.strip("\n"))
        while lengeh:
            line = int(D.readline().strip("\n"))
            L.append(line)
            lengeh -= 1
    D.close()
    return L, length2


def BulbleSort(List, n):  # 冒泡排序法
    for i in range(1, n):
        for j in range(0, n - i):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
    return List


def merge(a, b):  # 合并俩个数组
    result = []
    L = R = 0
    while L < len(a) and R < len(b):
        if a[L] < b[R]:
            result.append(a[L])
            L += 1
        else:
            result.append(b[R])
            R += 1
    if L == len(a):
        for i in b[R:]:
            result.append(i)
    else:
        for i in a[L:]:
            result.append(i)
    return result


def merge_sort(List):  # 合并排序
    if len(List) <= 1:
        return List
    middle = len(List) // 2
    left = merge_sort(List[:middle])
    right = merge_sort(List[middle:])
    return merge(left, right)


def main():
    List2 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,
             11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000,
             20000]

    data = {}  # 字典，记录里不同数据量的排序时间

    for i in List2:
        Str = r'G:\algo\dataset\data_{}.txt'.format(i)
        L, n = OpenFile(Str)
        start = time.time()
        # BulbleSort(L, n)
        merge_sort(L)
        end = time.time()
        t = end - start
        data[i] = t
    print(data)


main()