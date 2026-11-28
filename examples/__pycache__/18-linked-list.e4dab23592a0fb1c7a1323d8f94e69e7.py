
# apl-source:1
# مثال 18 — قائمة مرتبطة
# apl-source:2
# Linked List Implementation
# apl-source:3
# Demonstrates: classes, recursion, self-reference, data structures
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/18-linked-list.apl
# apl-source:6

# apl-source:7
class العقدة:
    # apl-source:8
    def __init__(ذات, قيمة):
        # apl-source:9
        ذات.قيمة = قيمة
        # apl-source:10
        ذات.التالي = None
# apl-source:11

# apl-source:12
class قائمة_مربوطة:
    # apl-source:13
    def __init__(ذات):
        # apl-source:14
        ذات.رأس = None
        # apl-source:15
        ذات.الطول = 0
# apl-source:16

    # apl-source:17
    def إضافة(ذات, قيمة):
        # apl-source:18
        عقدة = العقدة(قيمة)
        # apl-source:19
        if ذات.رأس == None:
            # apl-source:20
            ذات.رأس = عقدة
        # apl-source:21
        else:
            # apl-source:22
            مؤشر = ذات.رأس
            # apl-source:23
            while مؤشر.التالي != None:
                # apl-source:24
                مؤشر = مؤشر.التالي
            # apl-source:25
            مؤشر.التالي = عقدة
        # apl-source:26
        ذات.الطول = ذات.الطول + 1
# apl-source:27

    # apl-source:28
    def عرض(ذات):
        # apl-source:29
        if ذات.رأس == None:
            # apl-source:30
            return "(فارغة)"
        # apl-source:31
        نص_الناتج = ""
        # apl-source:32
        مؤشر = ذات.رأس
        # apl-source:33
        while مؤشر != None:
            # apl-source:34
            نص_الناتج = نص_الناتج + str(مؤشر.قيمة) + " -> "
            # apl-source:35
            مؤشر = مؤشر.التالي
        # apl-source:36
        return نص_الناتج + "None"
# apl-source:37

# apl-source:38
القائمة_مربوطة = قائمة_مربوطة()
# apl-source:39
for قيمة in [10, 20, 30, 40, 50]:
    # apl-source:40
    القائمة_مربوطة.إضافة(قيمة)
# apl-source:41

# apl-source:42
print("=== قائمة مرتبطة ===")
# apl-source:43
print("محتوى القائمة: " + القائمة_مربوطة.عرض())
# apl-source:44
print("الطول (متغير):  " + str(القائمة_مربوطة.الطول))
# apl-source:45
def عد_العقد(عقدة):
    # apl-source:46
    if عقدة == None:
        # apl-source:47
        return 0
    # apl-source:48
    return 1 + عد_العقد(عقدة.التالي)
# apl-source:49

# apl-source:50
print("الطول (متكرر):  " + str(عد_العقد(القائمة_مربوطة.رأس)))
# apl-source:51
