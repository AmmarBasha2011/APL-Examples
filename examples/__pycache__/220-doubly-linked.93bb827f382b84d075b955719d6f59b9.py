
# apl-source:1
# مثال 220 — القائمة المترابطة المزدوجة
# apl-source:2
# Doubly linked list
# apl-source:3
# Demonstrates: عقد باتجاهين، جولة أمامية وخلفية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/220-doubly-linked.apl
# apl-source:6

# apl-source:7
class عقدة:
    # apl-source:8
    def __init__(ذات, قيمة):
        # apl-source:9
        ذات.قيمة = قيمة
        # apl-source:10
        ذات.التالي = None
        # apl-source:11
        ذات.السابق = None
# apl-source:12

# apl-source:13
class قائمة_مزدوجة:
    # apl-source:14
    def __init__(ذات):
        # apl-source:15
        ذات.رأس = None
        # apl-source:16
        ذات.ذيل = None
# apl-source:17

    # apl-source:18
    def أضف_نهاية(ذات, قيمة):
        # apl-source:19
        جديدة = عقدة(قيمة)
        # apl-source:20
        if ذات.ذيل == None:
            # apl-source:21
            ذات.رأس = جديدة
            # apl-source:22
            ذات.ذيل = جديدة
            # apl-source:23
            return
        # apl-source:24
        ذات.ذيل.التالي = جديدة
        # apl-source:25
        جديدة.السابق = ذات.ذيل
        # apl-source:26
        ذات.ذيل = جديدة
# apl-source:27

    # apl-source:28
    def أمامية(ذات):
        # apl-source:29
        عناصر = []
        # apl-source:30
        حالي = ذات.رأس
        # apl-source:31
        while حالي != None:
            # apl-source:32
            عناصر.append(حالي.قيمة)
            # apl-source:33
            حالي = حالي.التالي
        # apl-source:34
        return عناصر
# apl-source:35

    # apl-source:36
    def خلفية(ذات):
        # apl-source:37
        عناصر = []
        # apl-source:38
        حالي = ذات.ذيل
        # apl-source:39
        while حالي != None:
            # apl-source:40
            عناصر.append(حالي.قيمة)
            # apl-source:41
            حالي = حالي.السابق
        # apl-source:42
        return عناصر
# apl-source:43

# apl-source:44
ق = قائمة_مزدوجة()
# apl-source:45
ق.أضف_نهاية(1)
# apl-source:46
ق.أضف_نهاية(2)
# apl-source:47
ق.أضف_نهاية(3)
# apl-source:48
print("أمامية:", ق.أمامية())
# apl-source:49
print("خلفية:", ق.خلفية())
# apl-source:50
