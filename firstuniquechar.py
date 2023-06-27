from collections import Counter
def firstUniqueChar(s):
    counter=Counter(s)
    for i in range(len(s)):
        if counter[s[i]]==1:
            return i
    return -1


s=str(input("Enter the input string : "))
print(f"Answer is : {firstUniqueChar(s)}")