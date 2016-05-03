def NPalindromes(s):
    result = []
    for i in range(0, len(s)):
        # Check for odd palindromes
        start_ix, end_ix = i - 1, i + 1
        while start_ix >= 0 and end_ix < len(s) and s[start_ix] == s[end_ix]:
            result.append(s[start_ix:end_ix+1])
            start_ix -= 1
            end_ix += 1
        
        # Check for even palindromes
        start_ix, end_ix = i, i + 1
        while start_ix >= 0 and end_ix < len(s) and s[start_ix] == s[end_ix]:
            result.append(s[start_ix:end_ix+1])
            start_ix -= 1
            end_ix += 1
    return len(result)

print NPalindromes('ababa')
print NPalindromes('abba')