
# apl-source:1
# مثال 2390 — صنف حساب بنكي بسقف سحب
# apl-source:2
# Bank account with withdraw limit
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2390-class-bank-account-deposit-withdraw-limit.apl
# apl-source:6

# apl-source:7
# # نعرف صنفا
# apl-source:8
# # ونختبر سلوكه
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
class حساب:
    # apl-source:19
    def __init__(ذات, ر):
        # apl-source:20
        ذات.ر = ر
# apl-source:21

    # apl-source:22
    def ايداع(ذات, م):
        # apl-source:23
        ذات.ر = ذات.ر + م
# apl-source:24

    # apl-source:25
    def سحب(ذات, م):
        # apl-source:26
        if م > ذات.ر:
            # apl-source:27
            return False
        # apl-source:28
        ذات.ر = ذات.ر - م
        # apl-source:29
        return True
# apl-source:30

# apl-source:31
ح = حساب(100)
# apl-source:32
ح.ايداع(50)
# apl-source:33
تأكد_يساوي(ح.ر, 150, "بعد الإيداع")
# apl-source:34
تأكد_يساوي(ح.سحب(200), False, "سحب زائد")
# apl-source:35
تأكد_يساوي(ح.سحب(30), True, "سحب مقبول")
# apl-source:36
تأكد_يساوي(ح.ر, 120, "الرصيد")
# apl-source:37
