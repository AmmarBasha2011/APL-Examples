
# apl-source:1
# مثال 368 — القوة بالعودية
# apl-source:2
# Recursive power
# apl-source:3
# Demonstrates: تقسيم الأس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/368-power-rec.apl
# apl-source:6

# apl-source:7
def قوة(قاعدة, أس):
    # apl-source:8
    if أس == 0:
        # apl-source:9
        return 1
    # apl-source:10
    if أس % 2 == 0:
        # apl-source:11
        نصف = قوة(قاعدة, أس // 2)
        # apl-source:12
        return نصف * نصف
    # apl-source:13
    return قاعدة * قوة(قاعدة, أس - 1)
# apl-source:14

# apl-source:15
print("2^8 =", قوة(2, 8))
# apl-source:16
print("3^4 =", قوة(3, 4))
# apl-source:17
print("9^0 =", قوة(9, 0))
# apl-source:18
