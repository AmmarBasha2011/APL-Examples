
# apl-source:1
# مثال 5120 — مجموع الأرقام ثم الباقي على 7
# apl-source:2
# Digit sum mod 7
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5120-digit-sum-mod-7.apl
# apl-source:6

# apl-source:7
# نفصل الأرقام بالقسمة على 10
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
  م = 0
  # apl-source:19
  while ن > 0:
    # apl-source:20
    م = م + ن % 10
    # apl-source:21
    ن = ن // 10
  # apl-source:22
  return م % 7
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(9), 2, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(123), 6, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(99999), 3, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(40507), 2, "حالة 5")
# apl-source:29
