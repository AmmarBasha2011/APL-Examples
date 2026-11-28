
# apl-source:1
# مثال 323 — أزواج متتالية
# apl-source:2
# Pairwise iteration
# apl-source:3
# Demonstrates: عنصر والذي يليه
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/323-pairwise.apl
# apl-source:6

# apl-source:7
def أزواج(قائمة):
    # apl-source:8
    نتيجة = []
    # apl-source:9
    for ي in range(len(قائمة) - 1):
        # apl-source:10
        نتيجة.append([قائمة[ي], قائمة[ي + 1]])
    # apl-source:11
    return نتيجة
# apl-source:12

# apl-source:13
print(أزواج([1, 2, 3, 4]))
# apl-source:14

# apl-source:15
فروق = [زوج[1] - زوج[0] for زوج in أزواج([10, 13, 17, 18])]
# apl-source:16
print("الفروق:", فروق)
# apl-source:17
