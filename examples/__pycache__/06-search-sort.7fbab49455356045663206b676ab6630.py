
# apl-source:1
# مثال 6 — خوارزميات البحث والترتيب
# apl-source:2
# Searching & Sorting Algorithms
# apl-source:3
# Demonstrates: custom functions, nested while-loops, list copy, mutation
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/06-search-sort.apl
# apl-source:6

# apl-source:7
def فقاعة(المدخل):
    # apl-source:8
    الناتج = المدخل.copy()
    # apl-source:9
    n = len(الناتج)
    # apl-source:10
    i = 0
    # apl-source:11
    while i < n:
        # apl-source:12
        j = 0
        # apl-source:13
        while j < n - 1 - i:
            # apl-source:14
            if الناتج[j] > الناتج[j + 1]:
                # apl-source:15
                مؤقت = الناتج[j]
                # apl-source:16
                الناتج[j] = الناتج[j + 1]
                # apl-source:17
                الناتج[j + 1] = مؤقت
            # apl-source:18
            j = j + 1
        # apl-source:19
        i = i + 1
    # apl-source:20
    return الناتج
# apl-source:21

# apl-source:22
def بحث(القائمة, الهدف):
    # apl-source:23
    رقم = 0
    # apl-source:24
    while رقم < len(القائمة):
        # apl-source:25
        if القائمة[رقم] == الهدف:
            # apl-source:26
            return رقم
        # apl-source:27
        رقم = رقم + 1
    # apl-source:28
    return -1
# apl-source:29

# apl-source:30
البيانات = [64, 25, 12, 22, 11, 90, 33]
# apl-source:31

# apl-source:32
print("=== البحث والترتيب ===")
# apl-source:33
print("الأصل: " + str(البيانات))
# apl-source:34
المرتب = فقاعة(البيانات)
# apl-source:35
print("مرتب: " + str(المرتب))
# apl-source:36
print("")
# apl-source:37
print("بحث عن 22: الفهرس " + str(بحث(البيانات, 22)))
# apl-source:38
print("بحث عن 99: الفهرس " + str(بحث(البيانات, 99)))
# apl-source:39
print("أكبر عنصر: " + str(المرتب[len(المرتب) - 1]))
# apl-source:40
print("أصغر عنصر: " + str(المرتب[0]))
# apl-source:41
