
# apl-source:1
# مثال 215 — شجرة البحث الثنائية
# apl-source:2
# Binary search tree
# apl-source:3
# Demonstrates: إدراج وبحث عوديان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/215-bst.apl
# apl-source:6

# apl-source:7
class عقدة:
    # apl-source:8
    def __init__(ذات, قيمة):
        # apl-source:9
        ذات.قيمة = قيمة
        # apl-source:10
        ذات.أيسر = None
        # apl-source:11
        ذات.أيمن = None
# apl-source:12

# apl-source:13
def أدرج_عقدة(ع, قيمة):
    # apl-source:14
    if ع == None:
        # apl-source:15
        return عقدة(قيمة)
    # apl-source:16
    if قيمة < ع.قيمة:
        # apl-source:17
        ع.أيسر = أدرج_عقدة(ع.أيسر, قيمة)
    # apl-source:18
    elif قيمة > ع.قيمة:
        # apl-source:19
        ع.أيمن = أدرج_عقدة(ع.أيمن, قيمة)
    # apl-source:20
    return ع
# apl-source:21

# apl-source:22
def ابحث_عقدة(عقدة, قيمة):
    # apl-source:23
    if عقدة == None:
        # apl-source:24
        return False
    # apl-source:25
    if عقدة.قيمة == قيمة:
        # apl-source:26
        return True
    # apl-source:27
    if قيمة < عقدة.قيمة:
        # apl-source:28
        return ابحث_عقدة(عقدة.أيسر, قيمة)
    # apl-source:29
    return ابحث_عقدة(عقدة.أيمن, قيمة)
# apl-source:30

# apl-source:31
def جولة_داخلية(عقدة, نتيجة):
    # apl-source:32
    if عقدة == None:
        # apl-source:33
        return
    # apl-source:34
    جولة_داخلية(عقدة.أيسر, نتيجة)
    # apl-source:35
    نتيجة.append(عقدة.قيمة)
    # apl-source:36
    جولة_داخلية(عقدة.أيمن, نتيجة)
# apl-source:37

# apl-source:38
جذر = None
# apl-source:39
for ق in [50, 30, 70, 20, 40, 60, 80]:
    # apl-source:40
    جذر = أدرج_عقدة(جذر, ق)
# apl-source:41

# apl-source:42
مرتبة = []
# apl-source:43
جولة_داخلية(جذر, مرتبة)
# apl-source:44
print("الجولة الداخلية (مرتبة):", مرتبة)
# apl-source:45
print("هل 40 موجود؟", ابحث_عقدة(جذر, 40))
# apl-source:46
print("هل 90 موجود؟", ابحث_عقدة(جذر, 90))
# apl-source:47
