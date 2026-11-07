student = {
    "name": "张三",
    "age": 20,
    "score": 85,
}

print(student["name"])
print(student["age"])
student["khy"] = "pig"
for a in student:
    print(a)

for k in student.values():
    print(k)

for i, j in student.items():
    print(i, j)

count = {}
for shu in ["a", "b", "b", "a", "a", "c"]:
    if shu in count:
        count[shu] = count[shu] + 1
    else:
        count[shu] = 1

print(count)

votes = ["张三", "李四", "张三", "王五", "张三", "李四"]
tongji = {}
for a in votes:
    if a in tongji:
        tongji[a] = tongji[a] + 1
    else:
        tongji[a] = 1
print(tongji)
zuida1 = 0
for i, j in tongji.items():
    print(f"{i}:{j}票")
    if j > zuida1:
        zuida1 = j
        a = i
print(f"得票最多：{a}，{zuida1}票")
zuida = max(tongji.values())
print(zuida)
