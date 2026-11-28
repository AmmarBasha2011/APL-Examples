
# apl-source:1
# مثال 1689 — مجموع البتات المضاءة في مدى
# apl-source:2
# Total set bits from 1 to n
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1689-count-set-bits-in-range.apl
# apl-source:6

# apl-source:7
# نعد بتات كل عدد بالإزاحة
# apl-source:8
# نجمع حتى ن
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
def بتات_العدد(ن):
  # apl-source:19
  عد = 0
  # apl-source:20
  while ن > 0:
    # apl-source:21
    عد = عد + (ن & 1)
    # apl-source:22
    ن = ن >> 1
  # apl-source:23
  return عد
# apl-source:24

# apl-source:25
def بتات_المدى(ن):
  # apl-source:26
  مجموع = 0
  # apl-source:27
  for ك in range(1, ن + 1):
    # apl-source:28
    مجموع = مجموع + بتات_العدد(ك)
  # apl-source:29
  return مجموع
# apl-source:30

# apl-source:31
تأكد_يساوي(بتات_المدى(1), 1, "واحد")
# apl-source:32
تأكد_يساوي(بتات_المدى(3), 4, "ثلاثة")
# apl-source:33
تأكد_يساوي(بتات_المدى(8), 13, "ثمانية")
# apl-source:34
