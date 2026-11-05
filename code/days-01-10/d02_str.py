s="flame"
print(s[0])
print(s[-1])
print(s[1:4])
print(s[:3])
print(s[:])
print(s[::2])
print(s[::-1])
print(len(s))
print(" khy ".strip())
print("a b c".split())
part="a b c".split()
print(part[0])
print("khy is baby".replace("baby","pig"))
print("khy is pig".endswith("pig"))
print("khy is pig".upper())
filename = "radar_20251012_2.1m_noFire_run03.bin"
parts=filename.split("_")
day=parts[1]
year=day[:4]
mo=day[4:6]
ri=day[6:8]
print(f"日期：{year}-{mo}-{ri}\n状态：{parts[3]}\n距离：{parts[2]}\n序号：{parts[4].replace(".bin","")}")