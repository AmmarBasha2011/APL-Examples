
# apl-source:1
# مثال 315 — المتتالية الحسابية
# apl-source:2
# Arithmetic sequence
# apl-source:3
# Demonstrates: الحد النوني والمجموع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/315-arithmetic-sequence.apl
# apl-source:6

# apl-source:7
def حد_نوني(أول, فرق, ن):
    # apl-source:8
    return أول + (ن - 1) * فرق
# apl-source:9

# apl-source:10
def مجموع_حسابية(أول, فرق, ن):
    # apl-source:11
    return ن * (2 * أول + (ن - 1) * فرق) // 2
# apl-source:12

# apl-source:13
print("الحد العاشر (أول=3، فرق=2):", حد_نوني(3, 2, 10))
# apl-source:14
print("مجموع أول 10 حدود:", مجموع_حسابية(3, 2, 10))
# apl-source:15
print("مجموع 1 إلى 100:", مجموع_حسابية(1, 1, 100))
# apl-source:16
