
# apl-source:1
# مثال 177 — التطابق بالحالات (match/case)
# apl-source:2
# Pattern matching with match/case
# apl-source:3
# Demonstrates: حالة، قيمة، افتراضي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/177-match-case.apl
# apl-source:6

# apl-source:7
def صف_درجة(درجة):
    # apl-source:8
    match درجة:
        # apl-source:9
        case 10:
            # apl-source:10
            return "ممتاز"
        # apl-source:11
        case 9:
            # apl-source:12
            return "ممتاز"
        # apl-source:13
        case 8:
            # apl-source:14
            return "جيد جدا"
        # apl-source:15
        case 7:
            # apl-source:16
            return "جيد"
        # apl-source:17
        case _:
            # apl-source:18
            return "يحتاج تحسينا"
# apl-source:19

# apl-source:20
for د in [10, 8, 7, 4]:
    # apl-source:21
    print(د, "->", صف_درجة(د))
# apl-source:22

# apl-source:23
def نوع_يوم(رقم):
    # apl-source:24
    match رقم:
        # apl-source:25
        case 1:
            # apl-source:26
            return "بداية الأسبوع"
        # apl-source:27
        case 5:
            # apl-source:28
            return "نهاية الأسبوع"
        # apl-source:29
        case 6:
            # apl-source:30
            return "عطلة"
        # apl-source:31
        case 7:
            # apl-source:32
            return "عطلة"
        # apl-source:33
        case _:
            # apl-source:34
            return "يوم عادي"
# apl-source:35

# apl-source:36
print(نوع_يوم(6))
# apl-source:37
print(نوع_يوم(3))
# apl-source:38
