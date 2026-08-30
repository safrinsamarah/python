count = 0
total = 0

for i in range(1,21):
    if i % 4 == 0:
        count += 1
        total += i

print(f"count: {count}")
print(f"Sum: {total}")