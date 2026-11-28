
# apl-source:1
# مثال 297 — عنوان عمود إكسل
# apl-source:2
# Excel column title
# apl-source:3
# Demonstrates: تحويل أساس 26
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/297-excel-column.apl
# apl-source:6

# apl-source:7
def عمود_إكسل(عدد):
    # apl-source:8
    نتيجة = ""
    # apl-source:9
    while عدد > 0:
        # apl-source:10
        عدد = عدد - 1
        # apl-source:11
        نتيجة = chr(65 + عدد % 26) + نتيجة
        # apl-source:12
        عدد = عدد // 26
    # apl-source:13
    return نتيجة
# apl-source:14

# apl-source:15
print("1 =", عمود_إكسل(1))
# apl-source:16
print("28 =", عمود_إكسل(28))
# apl-source:17
print("701 =", عمود_إكسل(701))
# apl-source:18
print("702 =", عمود_إكسل(702))
# apl-source:19
