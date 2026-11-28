
# apl-source:1
# مثال 2156 — صنف مخزن بإضافة وسحب
# apl-source:2
# Inventory class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2156-inventory-class-add-remove-stock.apl
# apl-source:6

# apl-source:7
# # الإضافة تزيد الكمية
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
class مخزن:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.كميات = {}
# apl-source:21

    # apl-source:22
    def اضف(ذات, صنف_, كمية):
        # apl-source:23
        ذات.كميات[صنف_] = ذات.كميات.get(صنف_, 0) + كمية
# apl-source:24

    # apl-source:25
    def اسحب(ذات, صنف_, كمية):
        # apl-source:26
        if ذات.كميات.get(صنف_, 0) < كمية:
            # apl-source:27
            return False
        # apl-source:28
        ذات.كميات[صنف_] = ذات.كميات[صنف_] - كمية
        # apl-source:29
        return True
# apl-source:30

    # apl-source:31
    def متاح(ذات, صنف_):
        # apl-source:32
        return ذات.كميات.get(صنف_, 0)
# apl-source:33

# apl-source:34
م = مخزن()
# apl-source:35
م.اضف("pen", 10)
# apl-source:36
تأكد_يساوي(م.اسحب("pen", 4), True, "سحب")
# apl-source:37
تأكد_يساوي(م.متاح("pen"), 6, "المتبقي")
# apl-source:38
تأكد_يساوي(م.اسحب("pen", 7), False, "فشل")
# apl-source:39
تأكد_يساوي(م.متاح("cup"), 0, "غير موجود")
# apl-source:40
