
# apl-source:1
# مثال 1126 — آلة بيع
# apl-source:2
# Vending machine with change
# apl-source:3
# Demonstrates: آلة حالات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1126-vending-machine.apl
# apl-source:6

# apl-source:7
# الآلة تجمع النقود حتى يبلغ السعر
# apl-source:8
# ثم تصرف المنتج وترد الباقي وتبدأ من جديد
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
class آلة_بيع:
    # apl-source:19
    def __init__(ذات, سعر):
        # apl-source:20
        ذات.سعر = سعر
        # apl-source:21
        ذات.رصيد = 0
        # apl-source:22
        ذات.مبيعات = 0
# apl-source:23

    # apl-source:24
    def ضع_نقود(ذات, مبلغ):
        # apl-source:25
        ذات.رصيد = ذات.رصيد + مبلغ
        # apl-source:26
        if ذات.رصيد >= ذات.سعر:
            # apl-source:27
            باقي = ذات.رصيد - ذات.سعر
            # apl-source:28
            ذات.رصيد = 0
            # apl-source:29
            ذات.مبيعات = ذات.مبيعات + 1
            # apl-source:30
            return باقي
        # apl-source:31
        return -1
# apl-source:32

# apl-source:33
آ = آلة_بيع(75)
# apl-source:34
تأكد_يساوي(آ.ضع_نقود(50), -1, "ينتظر")
# apl-source:35
تأكد_يساوي(آ.ضع_نقود(25), 0, "صرف بلا باقي")
# apl-source:36
تأكد_يساوي(آ.ضع_نقود(100), 25, "صرف مع باقي")
# apl-source:37
تأكد_يساوي(آ.مبيعات, 2, "عدد المبيعات")
# apl-source:38
تأكد_يساوي(آ.رصيد, 0, "الرصيد مصفر")
# apl-source:39
