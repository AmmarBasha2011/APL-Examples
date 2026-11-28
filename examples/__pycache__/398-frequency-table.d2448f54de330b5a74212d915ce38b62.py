
# apl-source:1
# مثال 398 — جدول التكرار
# apl-source:2
# Frequency table
# apl-source:3
# Demonstrates: تكرار النسب المئوية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/398-frequency-table.apl
# apl-source:6

# apl-source:7
بيانات = ["أ", "ب", "أ", "ج", "أ", "ب", "أ", "ب", "ج"]
# apl-source:8
تكرار = {}
# apl-source:9
for ق in بيانات:
    # apl-source:10
    قديم = تكرار.get(ق, 0)
    # apl-source:11
    تكرار[ق] = قديم + 1
# apl-source:12

# apl-source:13
مفاتيح = sorted(تكرار.keys())
# apl-source:14
for مفتاح in مفاتيح:
    # apl-source:15
    نسبة = تكرار[مفتاح] / len(بيانات) * 100
    # apl-source:16
    print(مفتاح + ":", تكرار[مفتاح], "مرة", "(" + str(نسبة) + "%)")
# apl-source:17
