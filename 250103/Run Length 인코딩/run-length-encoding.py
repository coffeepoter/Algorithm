def run_length_encoding(s):
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    
    result.append(s[-1] + str(count))
    
    encoded_string = ''.join(result)
    return len(encoded_string), encoded_string

A = input()

length, encoded = run_length_encoding(A)

print(length)
print(encoded)
