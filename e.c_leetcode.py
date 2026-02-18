def roman_to_int(s):
    """
    :type s: str
    :rtype: int
    """
    num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(s)):
        if i < len(s)-1:
            if num[s[i]] < num[s[i+1]]:
                result -= num[s[i]]
            elif num[s[i]] >= num[s[i+1]]:
                result += num[s[i]]
        else:
            result += num[s[i]]
    return result

print(roman_to_int("LVIII"))
print(roman_to_int("III"))
print(roman_to_int("MCMXCIV"))