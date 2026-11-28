
# apl-source:1
# مثال 282 — التبديلات يدويا
# apl-source:2
# Permutations by hand
# apl-source:3
# Demonstrates: توليد كل الترتيبات بالتراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/282-permutations-manual.apl
# apl-source:6

# apl-source:7
def تبديلات(عناصر):
    # apl-source:8
    if len(عناصر) <= 1:
        # apl-source:9
        return [عناصر]
    # apl-source:10
    نتيجة = []
    # apl-source:11
    for ي in range(len(عناصر)):
        # apl-source:12
        باقي = عناصر[0:ي] + عناصر[ي + 1:]
        # apl-source:13
        for ترتيب in تبديلات(باقي):
            # apl-source:14
            نتيجة.append([عناصر[ي]] + ترتيب)
    # apl-source:15
    return نتيجة
# apl-source:16

# apl-source:17
print(تبديلات([1, 2, 3]))
# apl-source:18
print("عدد تبديلات 4 عناصر:", len(تبديلات([1, 2, 3, 4])))
# apl-source:19
