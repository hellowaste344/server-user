s = input("Enter same different types\n")
start = 0
max_len = 0
seen = {}
for end, char in enumerate(s):
    if char in seen:
        start = max(start, seen[char] + 1)
    seen[char] = end
    max_len = max(max_len, end - start + 1)
print(max_len) # 3 (abc)   
