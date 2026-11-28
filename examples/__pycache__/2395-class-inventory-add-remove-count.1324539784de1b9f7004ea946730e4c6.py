
# apl-source:1
# مثال 2395 — صنف مخزون
# apl-source:2
# Inventory class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2395-class-inventory-add-remove-count.apl
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
class مخزن:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.ق = {}
# apl-source:21

    # apl-source:22
    def اضف(ذات, ا, ك):
        # apl-source:23
        ذات.ق[ا] = ذات.ق.get(ا, 0) + ك
# apl-source:24

    # apl-source:25
    def ازل(ذات, ا, ك):
        # apl-source:26
        ذات.ق[ا] = ذات.ق.get(ا, 0) - ك
# apl-source:27

    # apl-source:28
    def كمية(ذات, ا):
        # apl-source:29
        return ذات.ق.get(ا, 0)
# apl-source:30

# apl-source:31
م = مخزن()
# apl-source:32
م.اضف("تفاح", 10)
# apl-source:33
م.اضف("تفاح", 5)
# apl-source:34
م.ازل("تفاح", 3)
# apl-source:35
تأكد_يساوي(م.كمية("تفاح"), 12, "تفاح")
# apl-source:36
تأكد_يساوي(م.كمية("موز"), 0, "غير موجود")
# apl-source:37
