
# apl-source:1
# مثال 185 — الترتيب الفقاعي
# apl-source:2
# Bubble sort
# apl-source:3
# Demonstrates: حلقات متداخلة، مقارنة وتبديل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/185-bubble-sort.apl
# apl-source:6

# apl-source:7
def فقاعي(قائمة):
    # apl-source:8
    ن = len(قائمة)
    # apl-source:9
    for ي in range(ن):
        # apl-source:10
        for ز in range(ن - ي - 1):
            # apl-source:11
            if قائمة[ز] > قائمة[ز + 1]:
                # apl-source:12
                مؤقت = قائمة[ز]
                # apl-source:13
                قائمة[ز] = قائمة[ز + 1]
                # apl-source:14
                قائمة[ز + 1] = مؤقت
    # apl-source:15
    return قائمة
# apl-source:16

# apl-source:17
أرقام = [64, 34, 25, 12, 22, 11, 90]
# apl-source:18
print("قبل:", أرقام)
# apl-source:19
print("بعد:", فقاعي(أرقام))
# apl-source:20
