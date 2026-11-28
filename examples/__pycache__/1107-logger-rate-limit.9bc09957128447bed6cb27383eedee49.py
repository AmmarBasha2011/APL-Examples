
# apl-source:1
# مثال 1107 — مسجل بحد معدل
# apl-source:2
# Logger rate limiter
# apl-source:3
# Demonstrates: آخر وقت طباعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1107-logger-rate-limit.apl
# apl-source:6

# apl-source:7
# نحفظ آخر وقت طبعنا فيه كل رسالة
# apl-source:8
# ونسمح بها ثانية إذا مرت عشر ثوانٍ على الأقل
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
class مسجل:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.رسائل = []
        # apl-source:21
        ذات.ازمنة = []
# apl-source:22

    # apl-source:23
    def يطبع(ذات, ث, رسالة):
        # apl-source:24
        if رسالة in ذات.رسائل:
            # apl-source:25
            ف = 0
            # apl-source:26
            while ذات.رسائل[ف] != رسالة:
                # apl-source:27
                ف = ف + 1
            # apl-source:28
            if ث >= (ذات.ازمنة[ف] + 10):
                # apl-source:29
                ذات.ازمنة[ف] = ث
                # apl-source:30
                return True
            # apl-source:31
            return False
        # apl-source:32
        ذات.رسائل = ذات.رسائل + [رسالة]
        # apl-source:33
        ذات.ازمنة = ذات.ازمنة + [ث]
        # apl-source:34
        return True
# apl-source:35

# apl-source:36
م = مسجل()
# apl-source:37
تأكد_يساوي(م.يطبع(1, "foo"), True, "foo الأولى")
# apl-source:38
تأكد_يساوي(م.يطبع(2, "bar"), True, "bar الأولى")
# apl-source:39
تأكد_يساوي(م.يطبع(3, "foo"), False, "foo مبكرة")
# apl-source:40
تأكد_يساوي(م.يطبع(8, "bar"), False, "bar مبكرة")
# apl-source:41
تأكد_يساوي(م.يطبع(10, "foo"), False, "foo عند عشرة")
# apl-source:42
تأكد_يساوي(م.يطبع(11, "foo"), True, "foo بعد عشر")
# apl-source:43
