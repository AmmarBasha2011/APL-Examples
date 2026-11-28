
# apl-source:1
# مثال 13 — عمليات المصفوفات
# apl-source:2
# Matrix Operations
# apl-source:3
# Demonstrates: nested lists, indexing, nested while-loops
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/13-matrix-ops.apl
# apl-source:6

# apl-source:7
def اطبع_مصفوفة(مصفوفة):
    # apl-source:8
    for صف in مصفوفة:
        # apl-source:9
        print("  " + str(صف))
# apl-source:10

# apl-source:11
def جمع_مصفوفتين(أ, ب):
    # apl-source:12
    النتيجة = []
    # apl-source:13
    صف = 0
    # apl-source:14
    while صف < len(أ):
        # apl-source:15
        صف_جديد = []
        # apl-source:16
        عمود = 0
        # apl-source:17
        while عمود < len(أ[صف]):
            # apl-source:18
            صف_جديد = صف_جديد + [أ[صف][عمود] + ب[صف][عمود]]
            # apl-source:19
            عمود = عمود + 1
        # apl-source:20
        النتيجة = النتيجة + [صف_جديد]
        # apl-source:21
        صف = صف + 1
    # apl-source:22
    return النتيجة
# apl-source:23

# apl-source:24
def ضرب_مصفوفتين(أ, ب):
    # apl-source:25
    النتيجة = []
    # apl-source:26
    صف = 0
    # apl-source:27
    while صف < len(أ):
        # apl-source:28
        صف_جديد = []
        # apl-source:29
        عمود = 0
        # apl-source:30
        while عمود < len(ب[0]):
            # apl-source:31
            مجموع = 0
            # apl-source:32
            ك = 0
            # apl-source:33
            while ك < len(أ[0]):
                # apl-source:34
                مجموع = مجموع + أ[صف][ك] * ب[ك][عمود]
                # apl-source:35
                ك = ك + 1
            # apl-source:36
            صف_جديد = صف_جديد + [مجموع]
            # apl-source:37
            عمود = عمود + 1
        # apl-source:38
        النتيجة = النتيجة + [صف_جديد]
        # apl-source:39
        صف = صف + 1
    # apl-source:40
    return النتيجة
# apl-source:41

# apl-source:42
الأولى = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# apl-source:43
الثانية = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# apl-source:44

# apl-source:45
print("=== عمليات المصفوفات ===")
# apl-source:46
print("المصفوفة الأولى:")
# apl-source:47
اطبع_مصفوفة(الأولى)
# apl-source:48
print("")
# apl-source:49
print("المصفوفة الثانية:")
# apl-source:50
اطبع_مصفوفة(الثانية)
# apl-source:51
print("")
# apl-source:52
print("مجموعهما:")
# apl-source:53
اطبع_مصفوفة(جمع_مصفوفتين(الأولى, الثانية))
# apl-source:54
print("")
# apl-source:55
print("حاصل ضربهما:")
# apl-source:56
اطبع_مصفوفة(ضرب_مصفوفتين(الأولى, الثانية))
# apl-source:57
