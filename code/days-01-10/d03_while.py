i = 1

while i < 11:
    print(f"{i}")
    i = i + 1
j = 1
sum = 0
while sum < 100:
    sum = sum + j
    j = j + 1
print(f"加到 {j - 1} 时和超过 100，此时和为 {sum}")

k = 0
while k < 20:
    k = k + 1
    if k % 2 == 0:
        continue

    print(k)
