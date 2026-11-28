
# apl-source:1
# مثال 294 — من أرقام عشرية إلى رومانية
# apl-source:2
# Integer to Roman
# apl-source:3
# Demonstrates: جدول قيم تنازلي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/294-int-to-roman.apl
# apl-source:6

# apl-source:7
def إلى_روماني(عدد):
    # apl-source:8
    جدول = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
    # apl-source:9
    نتيجة = ""
    # apl-source:10
    for زوج in جدول:
        # apl-source:11
        while عدد >= زوج[0]:
            # apl-source:12
            نتيجة = نتيجة + زوج[1]
            # apl-source:13
            عدد = عدد - زوج[0]
    # apl-source:14
    return نتيجة
# apl-source:15

# apl-source:16
print("3 =", إلى_روماني(3))
# apl-source:17
print("58 =", إلى_روماني(58))
# apl-source:18
print("1994 =", إلى_روماني(1994))
# apl-source:19
print("2024 =", إلى_روماني(2024))
# apl-source:20
