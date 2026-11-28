
# apl-source:1
# مثال 321 — تقسيم قائمة إلى قطع
# apl-source:2
# Chunk a list
# apl-source:3
# Demonstrates: تقطيع بحجم ثابت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/321-chunk-list.apl
# apl-source:6

# apl-source:7
def قطع(قائمة, حجم_القطعة):
    # apl-source:8
    نتيجة = []
    # apl-source:9
    ي = 0
    # apl-source:10
    while ي < len(قائمة):
        # apl-source:11
        نتيجة.append(قائمة[ي:ي + حجم_القطعة])
        # apl-source:12
        ي = ي + حجم_القطعة
    # apl-source:13
    return نتيجة
# apl-source:14

# apl-source:15
print(قطع([1, 2, 3, 4, 5, 6, 7], 3))
# apl-source:16
print(قطع(["أ", "ب", "ج", "د"], 2))
# apl-source:17
