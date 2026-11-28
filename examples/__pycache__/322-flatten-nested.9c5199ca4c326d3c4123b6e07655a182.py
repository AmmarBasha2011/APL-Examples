
# apl-source:1
# مثال 322 — تسطيح قائمة متداخلة (عودي)
# apl-source:2
# Flatten a nested list
# apl-source:3
# Demonstrates: عودية على العمق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/322-flatten-nested.apl
# apl-source:6

# apl-source:7
def سطح(عنصر, نتيجة):
    # apl-source:8
    if type(عنصر) == type([]):
        # apl-source:9
        for فرعي in عنصر:
            # apl-source:10
            سطح(فرعي, نتيجة)
    # apl-source:11
    else:
        # apl-source:12
        نتيجة.append(عنصر)
# apl-source:13

# apl-source:14
def تسطيح(قائمة):
    # apl-source:15
    نتيجة = []
    # apl-source:16
    سطح(قائمة, نتيجة)
    # apl-source:17
    return نتيجة
# apl-source:18

# apl-source:19
print(تسطيح([1, [2, [3, 4], 5], 6]))
# apl-source:20
print(تسطيح([["أ"], ["ب", ["ج"]]]))
# apl-source:21
