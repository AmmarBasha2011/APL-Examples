
# apl-source:1
# مثال 5038 — هل القيمة داخل المدى [10, 20]؟
# apl-source:2
# Is value in range [10,20]
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5038-in-range-10-20-p.apl
# apl-source:6

# apl-source:7
# نقارن بالطرفين
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ن):
  # apl-source:18
  return ن >= 10 and ن <= 20
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(10), True, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(20), True, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(9), False, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(21), False, "حالة 4")
# apl-source:24
تأكد_يساوي(ف(15), True, "حالة 5")
# apl-source:25
