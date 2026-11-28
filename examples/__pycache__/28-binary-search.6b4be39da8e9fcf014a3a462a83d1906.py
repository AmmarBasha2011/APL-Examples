
# apl-source:1
# مثال 28 — البحث الثنائي
# apl-source:2
# Binary Search
# apl-source:3
# Demonstrates: while loops, division, sorted data, complexity
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/28-binary-search.apl
# apl-source:6

# apl-source:7
def دالة_بحث_ثنائي(القائمة, الهدف):
    # apl-source:8
    يسار = 0
    # apl-source:9
    يمين = len(القائمة) - 1
    # apl-source:10
    while يسار <= يمين:
        # apl-source:11
        الوسط = (يسار + يمين) // 2
        # apl-source:12
        if القائمة[الوسط] == الهدف:
            # apl-source:13
            return الوسط
        # apl-source:14
        if القائمة[الوسط] < الهدف:
            # apl-source:15
            يسار = الوسط + 1
        # apl-source:16
        else:
            # apl-source:17
            يمين = الوسط - 1
    # apl-source:18
    return -1
# apl-source:19

# apl-source:20
بحث_ثنائي = دالة_بحث_ثنائي
def دالة_بحث_خطي(القائمة, الهدف):
    # apl-source:21
    رقم = 0
    # apl-source:22
    while رقم < len(القائمة):
        # apl-source:23
        if القائمة[رقم] == الهدف:
            # apl-source:24
            return رقم
        # apl-source:25
        رقم = رقم + 1
    # apl-source:26
    return -1
# apl-source:27

# apl-source:28
بحث_خطي = دالة_بحث_خطي
البيانات = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
# apl-source:29

# apl-source:30
print("=== البحث الثنائي ===")
# apl-source:31
print("القائمة: " + str(البيانات))
# apl-source:32
print("")
# apl-source:33
print("--- بحث ثنائي ---")
# apl-source:34
for هدف in [1, 13, 25, 7, 99]:
    # apl-source:35
    فهرس = بحث_ثنائي(البيانات, هدف)
    # apl-source:36
    if فهرس == -1:
        # apl-source:37
        print("  " + str(هدف) + ": غير موجود")
    # apl-source:38
    else:
        # apl-source:39
        print("  " + str(هدف) + ": الفهرس " + str(فهرس))
# apl-source:40
print("")
# apl-source:41
print("--- مقارنة النتائج ---")
# apl-source:42
print("بحث 15 -> ثنائي: " + str(بحث_ثنائي(البيانات, 15)) + " | خطي: " + str(بحث_خطي(البيانات, 15)))
# apl-source:43
print("بحث 20 -> ثنائي: " + str(بحث_ثنائي(البيانات, 20)) + " | خطي: " + str(بحث_خطي(البيانات, 20)))
# apl-source:44
