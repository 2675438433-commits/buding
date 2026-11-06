filename = "khy is pig.bin"
filename = "radar_20251012_2.1m_noFire_run03.bin"
part = filename.split("_")
print(f"文件：{filename}\n")
if filename.endswith(".bin"):
    print("类型: 数据文件")
else:
    print("类型: 跳过")

if part[3] == "noFire":
    print("状态:无火")
else:
    print("状态:有火")

if float(part[2][:2]) <= 3:
    print(F"距离:{part[2]} 近距离")
else:
    print(F"距离:{part[2]} 远距离")
