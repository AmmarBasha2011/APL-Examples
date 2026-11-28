
# apl-source:1
# مثال 283 — توليد الأقواس المتوازنة
# apl-source:2
# Generate balanced parentheses
# apl-source:3
# Demonstrates: تراجع بشرطين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/283-generate-parentheses.apl
# apl-source:6

# apl-source:7
def ولد(حالية, مفتوحة, مغلقة, ن, نتيجة):
    # apl-source:8
    if len(حالية) == 2 * ن:
        # apl-source:9
        نتيجة.append(حالية)
        # apl-source:10
        return
    # apl-source:11
    if مفتوحة < ن:
        # apl-source:12
        ولد(حالية + "(", مفتوحة + 1, مغلقة, ن, نتيجة)
    # apl-source:13
    if مغلقة < مفتوحة:
        # apl-source:14
        ولد(حالية + ")", مفتوحة, مغلقة + 1, ن, نتيجة)
# apl-source:15

# apl-source:16
def أقواس(ن):
    # apl-source:17
    نتيجة = []
    # apl-source:18
    ولد("", 0, 0, ن, نتيجة)
    # apl-source:19
    return نتيجة
# apl-source:20

# apl-source:21
print(أقواس(3))
# apl-source:22
print("عدد حلول 4:", len(أقواس(4)))
# apl-source:23
