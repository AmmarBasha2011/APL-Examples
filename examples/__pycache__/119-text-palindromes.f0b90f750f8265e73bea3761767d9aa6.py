
# apl-source:1
# مثال 119 — كشف النصوص المتناظرة
# apl-source:2
# Palindrome detection
# apl-source:3
# Demonstrates: دوال، حلقات، شروط، دوال النصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/119-text-palindromes.apl
# apl-source:6

# apl-source:7
def متناظرة(نص):
    # apl-source:8
    نظيف = ""
    # apl-source:9
    for حرف in نص:
        # apl-source:10
        if حرف != " ":
            # apl-source:11
            نظيف = نظيف + حرف
    # apl-source:12
    return نظيف == نظيف[::-1]
# apl-source:13

# apl-source:14
عبارات = ["aba", "رادر", "مادام", "لغة", "12321", "APL"]
# apl-source:15
for عبارة in عبارات:
    # apl-source:16
    if متناظرة(عبارة):
        # apl-source:17
        print(عبارة, ": متناظرة")
    # apl-source:18
    else:
        # apl-source:19
        print(عبارة, ": ليست متناظرة")
# apl-source:20
