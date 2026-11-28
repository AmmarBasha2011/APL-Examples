
# apl-source:1
# مثال 316 — المتتالية الهندسية
# apl-source:2
# Geometric sequence
# apl-source:3
# Demonstrates: الحد النوني والمجموع الهندسي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/316-geometric-sequence.apl
# apl-source:6

# apl-source:7
def حد_هندسي(أول, نسبة, ن):
    # apl-source:8
    return أول * نسبة ** (ن - 1)
# apl-source:9

# apl-source:10
def مجموع_هندسية(أول, نسبة, ن):
    # apl-source:11
    if نسبة == 1:
        # apl-source:12
        return أول * ن
    # apl-source:13
    return أول * (نسبة ** ن - 1) // (نسبة - 1)
# apl-source:14

# apl-source:15
print("الحد الخامس (أول=2، نسبة=3):", حد_هندسي(2, 3, 5))
# apl-source:16
print("مجموع أول 5 حدود:", مجموع_هندسية(2, 3, 5))
# apl-source:17
print("مجموع قوى 2 العشر الأولى:", مجموع_هندسية(1, 2, 10))
# apl-source:18
