def compress(chars: list[str]) -> int:
    size = len(chars)
    if size < 2:
        return size
    i = j = 0
    while i < size:
        count = 1
        while i < size - 1 and chars[i] == chars[i + 1]:
            count += 1
            i += 1
        chars[j] = chars[i]
        j += 1
        if count > 1:
            for c in str(count):
                chars[j] = c
                j += 1
        i += 1
    return j

print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(compress(["a","a","b","b","c","c","c"]))