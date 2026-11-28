
# apl-source:1
# مثال 566 — قاطع الدائرة
# apl-source:2
# Circuit breaker
# apl-source:3
# Demonstrates: قاطع دائرة، حالات، تهدئة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/566-circuit-breaker.apl
# apl-source:6

# apl-source:7
def تأكد_يساوي(فعلي, متوقع, اسم):
    # apl-source:8
    if فعلي != متوقع:
        # apl-source:9
        print("فشل:", اسم, "| متوقع:", متوقع, "| فعلي:", فعلي)
        # apl-source:10
        قياسي_نظام_اخرج(1)
    # apl-source:11
    print("ناجح:", اسم)
# apl-source:12

# apl-source:13

# apl-source:14
# قاطع الدائرة: حماية من تكرار الفشل
# apl-source:15
class قاطع:
    # apl-source:16
    def __init__(ذات, عتبة, تهدئة):
        # apl-source:17
        ذات.عتبة = عتبة
        # apl-source:18
        ذات.تهدئة = تهدئة
        # apl-source:19
        ذات.فشل = 0
        # apl-source:20
        ذات.حالة = "مغلق"
        # apl-source:21
        ذات.منذ_فتح = 0
    # apl-source:22
    def ناد(ذات, تنجح):
        # apl-source:23
        if ذات.حالة == "مفتوح":
            # apl-source:24
            ذات.منذ_فتح = ذات.منذ_فتح + 1
            # apl-source:25
            if ذات.منذ_فتح < ذات.تهدئة:
                # apl-source:26
                return "مرفوض: القاطع مفتوح"
            # apl-source:27
            ذات.حالة = "نصف مفتوح"
        # apl-source:28
        if تنجح:
            # apl-source:29
            ذات.فشل = 0
            # apl-source:30
            ذات.حالة = "مغلق"
            # apl-source:31
            return "نجاح"
        # apl-source:32
        ذات.فشل = ذات.فشل + 1
        # apl-source:33
        if ذات.حالة == "نصف مفتوح" or ذات.فشل >= ذات.عتبة:
            # apl-source:34
            ذات.حالة = "مفتوح"
            # apl-source:35
            ذات.منذ_فتح = 0
        # apl-source:36
        return "فشل"
# apl-source:37

# apl-source:38
ق = قاطع(3, 2)
# apl-source:39
تأكد_يساوي(ق.ناد(False), "فشل", "فشل 1")
# apl-source:40
تأكد_يساوي(ق.ناد(False), "فشل", "فشل 2")
# apl-source:41
تأكد_يساوي(ق.ناد(False), "فشل", "فشل 3 يفتح")
# apl-source:42
تأكد_يساوي(ق.حالة, "مفتوح", "الحالة مفتوح")
# apl-source:43
تأكد_يساوي(ق.ناد(True), "مرفوض: القاطع مفتوح", "يرفض أثناء الفتح")
# apl-source:44
تأكد_يساوي(ق.ناد(True), "نجاح", "بعد التهدئة نصف مفتوح ثم نجاح")
# apl-source:45
تأكد_يساوي(ق.حالة, "مغلق", "عاد مغلقاً")
# apl-source:46
