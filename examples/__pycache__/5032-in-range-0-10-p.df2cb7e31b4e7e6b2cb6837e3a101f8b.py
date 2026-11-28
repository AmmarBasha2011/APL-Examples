
# apl-source:1
# مثال 5032 — هل القيمة داخل المدى [0, 10]؟
# apl-source:2
# Is value in range [0,10]
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5032-in-range-0-10-p.apl
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
  return ن >= 0 and ن <= 10
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(0), True, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(10), True, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(-1), False, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(11), False, "حالة 4")
# apl-source:24
تأكد_يساوي(ف(5), True, "حالة 5")
# apl-source:25
