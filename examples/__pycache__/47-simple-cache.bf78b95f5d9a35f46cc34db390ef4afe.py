
# apl-source:1
# مثال 47 — كاش بسيط من الصفر
# apl-source:2
# Simple Cache from Scratch
# apl-source:3
# Demonstrates: class, dict lookup, cache hit/miss counting
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/47-simple-cache.apl
# apl-source:6

# apl-source:7
class خزائن:
    # apl-source:8
    def __init__(ذات, حد):
        # apl-source:9
        ذات.البيانات = {}
        # apl-source:10
        ذات.الحد = حد
        # apl-source:11
        ذات.إصابات = 0
        # apl-source:12
        ذات.أخطاء = 0
# apl-source:13

    # apl-source:14
    def اجلب(ذات, مفتاح, رقم):
        # apl-source:15
        if مفتاح in ذات.البيانات:
            # apl-source:16
            ذات.إصابات = ذات.إصابات + 1
            # apl-source:17
            return ذات.البيانات[مفتاح]
        # apl-source:18
        ذات.أخطاء = ذات.أخطاء + 1
        # apl-source:19
        قيمة = رقم * رقم
        # apl-source:20
        ذات.البيانات[مفتاح] = قيمة
        # apl-source:21
        return قيمة
# apl-source:22

    # apl-source:23
    def إحصاء(ذات):
        # apl-source:24
        return "إصابات=" + str(ذات.إصابات) + " أخطاء=" + str(ذات.أخطاء)
# apl-source:25

# apl-source:26
def دالة_مربع(رقم):
    # apl-source:27
    return رقم * رقم
# apl-source:28

# apl-source:29
مربع = دالة_مربع
print("=== كاش بسيط ===")
# apl-source:30
print("")
# apl-source:31
مخزن = خزائن(100)
# apl-source:32

# apl-source:33
print("أول جلب لمربع(5): " + str(مخزن.اجلب("m1", 5)))
# apl-source:34
print("مربع(5) مرة ثانية: " + str(مخزن.اجلب("m1", 5)))
# apl-source:35
print("مربع(5) مرة ثالثة: " + str(مخزن.اجلب("m1", 5)))
# apl-source:36
print("")
# apl-source:37
print("مفتاح جديد مربع(7): " + str(مخزن.اجلب("m2", 7)))
# apl-source:38
print("")
# apl-source:39
print("الإحصاء: " + مخزن.إحصاء())
# apl-source:40
print("المفاتيح المخزنة: " + str(len(مخزن.البيانات)))
# apl-source:41
