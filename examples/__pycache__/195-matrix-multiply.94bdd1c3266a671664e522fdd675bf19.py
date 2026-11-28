
# apl-source:1
# مثال 195 — ضرب المصفوفات
# apl-source:2
# Matrix multiplication
# apl-source:3
# Demonstrates: حلقات ثلاثية، مصفوفات متداخلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/195-matrix-multiply.apl
# apl-source:6

# apl-source:7
def اضرب(أ, ب):
    # apl-source:8
    صفوف = len(أ)
    # apl-source:9
    أعمدة = len(ب[0])
    # apl-source:10
    داخل = len(ب)
    # apl-source:11
    نتيجة = []
    # apl-source:12
    for ي in range(صفوف):
        # apl-source:13
        صف = []
        # apl-source:14
        for ز in range(أعمدة):
            # apl-source:15
            مجموع = 0
            # apl-source:16
            for ك in range(داخل):
                # apl-source:17
                مجموع = مجموع + أ[ي][ك] * ب[ك][ز]
            # apl-source:18
            صف.append(مجموع)
        # apl-source:19
        نتيجة.append(صف)
    # apl-source:20
    return نتيجة
# apl-source:21

# apl-source:22
أ = [[1, 2], [3, 4]]
# apl-source:23
ب = [[5, 6], [7, 8]]
# apl-source:24
ن = اضرب(أ, ب)
# apl-source:25
print("النتيجة:", ن)
# apl-source:26
print("العنصر (0,0):", ن[0][0])
# apl-source:27
print("العنصر (1,1):", ن[1][1])
# apl-source:28
