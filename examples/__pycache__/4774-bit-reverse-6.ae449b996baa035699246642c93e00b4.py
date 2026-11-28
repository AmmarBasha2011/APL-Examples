
# apl-source:1
# مثال 4774 — عكس 6 بتات
# apl-source:2
# Reverse the lowest 6 bits
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4774-bit-reverse-6.apl
# apl-source:6

# apl-source:7
# نقرأ البتات من اليمين ونبني الناتج من اليسار
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
  ر = 0
  # apl-source:19
  for ي in range(6):
    # apl-source:20
    ر = ر * 2 + (ن % 2)
    # apl-source:21
    ن = ن // 2
  # apl-source:22
  return ر
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(1), 32, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(5), 40, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(63), 63, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(33), 33, "حالة 5")
# apl-source:29
