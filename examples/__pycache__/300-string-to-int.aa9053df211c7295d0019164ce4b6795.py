
# apl-source:1
# مثال 300 — تحويل نص إلى عدد (atoi)
# apl-source:2
# String to integer
# apl-source:3
# Demonstrates: تحليل يدوي مع إشارة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/300-string-to-int.apl
# apl-source:6

# apl-source:7
def حول_عدد(نص_الدخل):
    # apl-source:8
    نص_نظيف = نص_الدخل.strip()
    # apl-source:9
    if len(نص_نظيف) == 0:
        # apl-source:10
        return 0
    # apl-source:11
    إشارة = 1
    # apl-source:12
    ي = 0
    # apl-source:13
    if نص_نظيف[0] == "-":
        # apl-source:14
        إشارة = -1
        # apl-source:15
        ي = 1
    # apl-source:16
    elif نص_نظيف[0] == "+":
        # apl-source:17
        ي = 1
    # apl-source:18
    قيمة = 0
    # apl-source:19
    while ي < len(نص_نظيف) and نص_نظيف[ي] >= "0" and نص_نظيف[ي] <= "9":
        # apl-source:20
        قيمة = قيمة * 10 + ord(نص_نظيف[ي]) - 48
        # apl-source:21
        ي = ي + 1
    # apl-source:22
    return إشارة * قيمة
# apl-source:23

# apl-source:24
print(حول_عدد("42"))
# apl-source:25
print(حول_عدد("   -42"))
# apl-source:26
print(حول_عدد("4193 مع كلمات"))
# apl-source:27
print(حول_عدد("كلمات 987"))
# apl-source:28
