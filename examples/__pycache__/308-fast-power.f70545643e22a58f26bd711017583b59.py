
# apl-source:1
# مثال 308 — القوة السريعة
# apl-source:2
# Fast exponentiation
# apl-source:3
# Demonstrates: رفع بأسر لوغاريتمي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/308-fast-power.apl
# apl-source:6

# apl-source:7
def قوة_سريعة(أساس, أس):
    # apl-source:8
    نتيجة = 1
    # apl-source:9
    while أس > 0:
        # apl-source:10
        if أس % 2 == 1:
            # apl-source:11
            نتيجة = نتيجة * أساس
        # apl-source:12
        أساس = أساس * أساس
        # apl-source:13
        أس = أس // 2
    # apl-source:14
    return نتيجة
# apl-source:15

# apl-source:16
print("2^10 =", قوة_سريعة(2, 10))
# apl-source:17
print("3^5 =", قوة_سريعة(3, 5))
# apl-source:18
print("5^0 =", قوة_سريعة(5, 0))
# apl-source:19
print("2^100 لها", len(str(قوة_سريعة(2, 100))), "خانة")
# apl-source:20
