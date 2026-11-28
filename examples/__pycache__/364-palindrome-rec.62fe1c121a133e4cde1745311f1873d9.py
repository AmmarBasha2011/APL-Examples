
# apl-source:1
# مثال 364 — فحص التناظر بالعودية
# apl-source:2
# Recursive palindrome check
# apl-source:3
# Demonstrates: مقارنة الطرفين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/364-palindrome-rec.apl
# apl-source:6

# apl-source:7
def متناظر(نص_الدخل):
    # apl-source:8
    if len(نص_الدخل) <= 1:
        # apl-source:9
        return True
    # apl-source:10
    if نص_الدخل[0] != نص_الدخل[-1]:
        # apl-source:11
        return False
    # apl-source:12
    return متناظر(نص_الدخل[1:len(نص_الدخل) - 1])
# apl-source:13

# apl-source:14
print("level:", متناظر("level"))
# apl-source:15
print("abcba:", متناظر("abcba"))
# apl-source:16
print("hello:", متناظر("hello"))
# apl-source:17
