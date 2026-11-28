
# apl-source:1
# مثال 4691 — قائمة الأعداد التقبل القسمة على 4 ولا على 6 حتى حد معين
# apl-source:2
# Numbers up to a limit: list of the divisible by 4 but not 6 ones
# apl-source:3
# Demonstrates: حلقات وشروط وأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4691-numbers-list-div4not6.apl
# apl-source:6

# apl-source:7
# نفحص الأعداد من 1 إلى الحد
# apl-source:8
# ونجمع منها اللي يحقق الشرط
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
def ف(ح):
  # apl-source:19
  ن = []
  # apl-source:20
  for ر in range(1, ح + 1):
    # apl-source:21
    if ر % 4 == 0 and ر % 6 != 0:
      # apl-source:22
      ن = ن + [ر]
  # apl-source:23
  return ن
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(28), [4, 8, 16, 20, 28], "حالة 1")
# apl-source:26
تأكد_يساوي(ف(42), [4, 8, 16, 20, 28, 32, 40], "حالة 2")
# apl-source:27
تأكد_يساوي(ف(79), [4, 8, 16, 20, 28, 32, 40, 44, 52, 56, 64, 68, 76], "حالة 3")
# apl-source:28
تأكد_يساوي(ف(1), [], "حالة 4")
# apl-source:29
تأكد_يساوي(ف(0), [], "حالة 5")
# apl-source:30
