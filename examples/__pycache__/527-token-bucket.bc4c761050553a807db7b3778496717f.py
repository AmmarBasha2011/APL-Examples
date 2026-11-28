
# apl-source:1
# مثال 527 — دلو الرموز
# apl-source:2
# Token bucket rate limiter
# apl-source:3
# Demonstrates: دلو رموز، تحديد معدل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/527-token-bucket.apl
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
# دلو الرموز: محدد معدل الطلبات
# apl-source:15
class دلو_رموز:
    # apl-source:16
    def __init__(ذات, سعة, معدل):
        # apl-source:17
        ذات.سعة = سعة
        # apl-source:18
        ذات.رموز = سعة
        # apl-source:19
        ذات.معدل = معدل
    # apl-source:20
    def تعبئة(ذات, ثوان):
        # apl-source:21
        ذات.رموز = min(ذات.سعة, ذات.رموز + ثوان * ذات.معدل)
    # apl-source:22
    def اسمح(ذات):
        # apl-source:23
        if ذات.رموز >= 1:
            # apl-source:24
            ذات.رموز = ذات.رموز - 1
            # apl-source:25
            return True
        # apl-source:26
        return False
# apl-source:27

# apl-source:28
دلو = دلو_رموز(3, 1)
# apl-source:29
تأكد_يساوي(دلو.اسمح(), True, "أول طلب")
# apl-source:30
تأكد_يساوي(دلو.اسمح(), True, "ثاني طلب")
# apl-source:31
تأكد_يساوي(دلو.اسمح(), True, "ثالث طلب")
# apl-source:32
تأكد_يساوي(دلو.اسمح(), False, "الرابع مرفوض")
# apl-source:33
دلو.تعبئة(2)
# apl-source:34
تأكد_يساوي(دلو.اسمح(), True, "بعد ثانيتين")
# apl-source:35
تأكد_يساوي(دلو.رموز, 1, "بقي رمز واحد")
# apl-source:36
