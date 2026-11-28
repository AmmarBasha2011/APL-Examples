
# apl-source:1
# مثال 4699 — قائمة الأعداد المجموع أرقامه زوجي حتى حد معين
# apl-source:2
# Numbers up to a limit: list of the even digit sum ones
# apl-source:3
# Demonstrates: حلقات وشروط وأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4699-numbers-list-digsum_even.apl
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
    if sum([int(د) for د in str(ر)]) % 2 == 0:
      # apl-source:22
      ن = ن + [ر]
  # apl-source:23
  return ن
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(13), [2, 4, 6, 8, 11, 13], "حالة 1")
# apl-source:26
تأكد_يساوي(ف(49), [2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 31, 33, 35, 37, 39, 40, 42, 44, 46, 48], "حالة 2")
# apl-source:27
تأكد_يساوي(ف(129), [2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 31, 33, 35, 37, 39, 40, 42, 44, 46, 48, 51, 53, 55, 57, 59, 60, 62, 64, 66, 68, 71, 73, 75, 77, 79, 80, 82, 84, 86, 88, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 110, 112, 114, 116, 118, 121, 123, 125, 127, 129], "حالة 3")
# apl-source:28
تأكد_يساوي(ف(1), [], "حالة 4")
# apl-source:29
تأكد_يساوي(ف(0), [], "حالة 5")
# apl-source:30
