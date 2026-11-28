
# apl-source:1
# مثال 2373 — الثبات الضربي
# apl-source:2
# Multiplicative persistence
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2373-persistence-multiplicative-steps.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
  خ = 0
  # apl-source:20
  while ن >= 10:
    # apl-source:21
    ح = 1
    # apl-source:22
    for ر in str(ن):
      # apl-source:23
      ح = ح * int(ر)
    # apl-source:24
    ن = ح
    # apl-source:25
    خ = خ + 1
  # apl-source:26
  return خ
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(7), 0, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(39), 3, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(77), 4, "حالة 3")
# apl-source:31
تأكد_يساوي(ف(679), 5, "حالة 4")
# apl-source:32
تأكد_يساوي(ف(999), 4, "حالة 5")
# apl-source:33
