names = ["张三", "李四", "王五"]
print(",".join(names))

squares = [x * x for x in range(1, 6)]

scores = [78, 92, 65, 88, 95, 73, 59, 84, 91, 67]
tags = ["雷达", "视觉", "雷达", "融合", "视觉", "算法", "雷达"]
cjd = [str(x) for x in scores]
print(f"成绩单：{",".join(cjd)}")
jg = [str(x) for x in scores if x >= 60]
print(f"及格分数：{",".join(jg)}")
bjg = [str(x) for x in scores if x < 60]
print(f"不及格分数：{",".join(bjg)}")
biaoqian = set(tags)
print(f"标签种类：{len(biaoqian)}")
print(f"标签列表：{",".join(biaoqian)}")
