
# apl-source:1
# مثال 1507 — عدد إلى نص ثنائي
# apl-source:2
# Integer to binary string
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1507-integer-to-binary-string.apl
# apl-source:6

# apl-source:7
# نقسم على اثنين ونسجل الباقي
# apl-source:8
# نقرأ البواقي من الأخير للأول
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
def ثنائي(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return "0"
  # apl-source:21
  بتات = ""
  # apl-source:22
  while ن > 0:
    # apl-source:23
    بتات = str(ن % 2) + بتات
    # apl-source:24
    ن = ن // 2
  # apl-source:25
  return بتات
# apl-source:26

# apl-source:27
تأكد_يساوي(ثنائي(0), "0", "صفر")
# apl-source:28
تأكد_يساوي(ثنائي(5), "101", "خمسة")
# apl-source:29
تأكد_يساوي(ثنائي(255), "11111111", "255")
# apl-source:30
تأكد_يساوي(ثنائي(1024), "10000000000", "1024")
# apl-source:31
