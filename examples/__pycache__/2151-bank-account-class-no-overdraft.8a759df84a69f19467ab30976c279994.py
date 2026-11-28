
# apl-source:1
# مثال 2151 — حساب بنكي بلا سحب على المكشوف
# apl-source:2
# Bank account class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2151-bank-account-class-no-overdraft.apl
# apl-source:6

# apl-source:7
# # الإيداع يزيد الرصيد
# apl-source:8
# # والسحب يرجع نجاحا أو فشلا
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
    def __init__(ذات, رصيد):
        # apl-source:20
        ذات.رصيد = رصيد
# apl-source:21

    # apl-source:22
    def ايداع(ذات, مبلغ):
        # apl-source:23
        ذات.رصيد = ذات.رصيد + مبلغ
# apl-source:24

    # apl-source:25
    def سحب(ذات, مبلغ):
        # apl-source:26
        if مبلغ > ذات.رصيد:
            # apl-source:27
            return False
        # apl-source:28
        ذات.رصيد = ذات.رصيد - مبلغ
        # apl-source:29
        return True
# apl-source:30

# apl-source:31
ح = حساب(100)
# apl-source:32
تأكد_يساوي(ح.سحب(30), True, "سحب ناجح")
# apl-source:33
تأكد_يساوي(ح.رصيد, 70, "الرصيد")
# apl-source:34
تأكد_يساوي(ح.سحب(100), False, "سحب فاشل")
# apl-source:35
ح.ايداع(50)
# apl-source:36
تأكد_يساوي(ح.رصيد, 120, "بعد الإيداع")
# apl-source:37
