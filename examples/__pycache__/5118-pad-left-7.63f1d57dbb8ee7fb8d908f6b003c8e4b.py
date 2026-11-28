
# apl-source:1
# مثال 5118 — ملء النص من اليسار حتى عرض 7
# apl-source:2
# Left pad to width 7
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5118-pad-left-7.apl
# apl-source:6

# apl-source:7
# نضيف أصفاراً قبل النص
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
  ر = ن
  # apl-source:19
  while len(ر) < 7:
    # apl-source:20
    ر = "0" + ر
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف("7"), "0000007", "حالة 1")
# apl-source:24
تأكد_يساوي(ف("123"), "0000123", "حالة 2")
# apl-source:25
تأكد_يساوي(ف("1111111"), "1111111", "حالة 3")
# apl-source:26
تأكد_يساوي(ف(""), "0000000", "حالة 4")
# apl-source:27
