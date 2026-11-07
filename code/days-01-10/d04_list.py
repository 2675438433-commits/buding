a = [1, 2, 3]

# 末尾加一个 → [1, 2, 3, 4]
a.append(4)
# 在下标 1 处插入 → [1, 99, 2, 3, 4]
a.insert(1, 99)
# 删掉末尾，并把删掉的值返回 → [1, 99, 2, 3]
a.pop()
# 删掉下标 0 → [99, 2, 3]
a.pop(0)
# 按值删，删掉第一个等于 2 的 → [99, 3]
a.remove(2)

a.sort()
a.sort(reverse=True)

a.sort()  # 原地排序，a 变成 [1, 1, 3, 4, 5]
a.sort(reverse=True)  # 从大到小 → [5, 4, 3, 1, 1]

b = sorted(a)  # 不改 a，返回一个新的排好序的列表

a = [3, 1, 4, 1, 5]

print(len(a))  # 5      元素个数
print(sum(a))  # 14     求和
print(max(a))  # 5      最大值
print(min(a))  # 1      最小值

scores = [2, 3, 2, 6, 2, 55]

print(2 in scores)
print(scores.count(1))
print(scores.index(3))

for i, s in enumerate(scores):
    print(i, s)

scores = [78, 92, 65, 88, 95, 73, 59, 84, 91, 67]
bujige = []
renshu = 0
print(f"成绩单：{scores}")

for a in scores:
    #  print(a)
    if a >= 60:
        renshu = renshu + 1
    else:
        bujige.append(a)

print(f"人数：{len(scores)}")
print(f"总分：{sum(scores)}")
print(f"平均分：{sum(scores) / len(scores)}")
print(f"最高分：{max(scores)}")
print(f"最低分：{min(scores)}")
print(f"及格人数：{renshu}/ {len(scores)}")
print(f"不及格分数：{bujige}")

paixu = sorted(scores, reverse=True)
print(f"从高到低：{paixu}")

