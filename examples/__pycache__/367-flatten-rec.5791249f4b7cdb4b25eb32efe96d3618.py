
# apl-source:1
# مثال 367 — عد عناصر متداخلة بالعودية
# apl-source:2
# Count nested items recursively
# apl-source:3
# Demonstrates: عد عميق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/367-flatten-rec.apl
# apl-source:6

# apl-source:7
def عد_عميق(عنصر):
    # apl-source:8
    if type(عنصر) == type([]):
        # apl-source:9
        مجموع = 0
        # apl-source:10
        for فرعي in عنصر:
            # apl-source:11
            مجموع = مجموع + عد_عميق(فرعي)
        # apl-source:12
        return مجموع
    # apl-source:13
    return 1
# apl-source:14

# apl-source:15
print(عد_عميق([1, [2, 3], [4, [5, 6]]]))
# apl-source:16
print(عد_عميق([[["أ"]], ["ب", "ج"]]))
# apl-source:17
