
# apl-source:1
# مثال 431 — منسق جداول نصية
# apl-source:2
# Text table formatter
# apl-source:3
# Demonstrates: عرض الأعمدة والحدود
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/431-table-formatter.apl
# apl-source:6

# apl-source:7
def وسع_نص(نص_الدخل, عرض_مطلوب):
    # apl-source:8
    ناتج = نص_الدخل
    # apl-source:9
    while len(ناتج) < عرض_مطلوب:
        # apl-source:10
        ناتج = ناتج + " "
    # apl-source:11
    return ناتج
# apl-source:12

# apl-source:13
صفوف = [
    # apl-source:14
    ["الاسم", "العمر", "المدينة"],
    # apl-source:15
    ["عمار", "26", "المنصورة"],
    # apl-source:16
    ["سارة", "24", "القاهرة"]
# apl-source:17
]
# apl-source:18

# apl-source:19
for صف_جدول in صفوف:
    # apl-source:20
    print("| " + وسع_نص(صف_جدول[0], 12) + "| " + وسع_نص(صف_جدول[1], 6) + "| " + وسع_نص(صف_جدول[2], 12) + "|")
# apl-source:21
