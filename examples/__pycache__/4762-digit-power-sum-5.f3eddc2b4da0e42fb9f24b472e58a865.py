
# apl-source:1
# مثال 4762 — مجموع قوى الأرقام (القوة 5)
# apl-source:2
# Sum of digits raised to 5
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4762-digit-power-sum-5.apl
# apl-source:6

# apl-source:7
# نرفع كل رقم لقوة ثابتة
# apl-source:8
# ونجمع النتائج
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
def ف(ن):
  # apl-source:19
  ج = 0
  # apl-source:20
  for د in str(ن):
    # apl-source:21
    ج = ج + int(د) ** 5
  # apl-source:22
  return ج
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(9), 59049, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(153), 3369, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(407), 17831, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(9474), 77904, "حالة 5")
# apl-source:29
