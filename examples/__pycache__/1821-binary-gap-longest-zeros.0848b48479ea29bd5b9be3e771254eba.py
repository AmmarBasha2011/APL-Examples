
# apl-source:1
# مثال 1821 — أطول فجوة ثنائية
# apl-source:2
# Longest binary gap
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1821-binary-gap-longest-zeros.apl
# apl-source:6

# apl-source:7
# نتتبع آخر موضع لبت مضاء
# apl-source:8
# الفرق ناقص واحد هو الفجوة
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
def فجوة(ن):
  # apl-source:19
  أطول = 0
  # apl-source:20
  آخر = -1
  # apl-source:21
  موضع = 0
  # apl-source:22
  while ن > 0:
    # apl-source:23
    if ن & 1 == 1:
      # apl-source:24
      if آخر != -1:
        # apl-source:25
        أطول = max(أطول, موضع - آخر - 1)
      # apl-source:26
      آخر = موضع
    # apl-source:27
    ن = ن >> 1
    # apl-source:28
    موضع = موضع + 1
  # apl-source:29
  return أطول
# apl-source:30

# apl-source:31
تأكد_يساوي(فجوة(9), 2, "1001")
# apl-source:32
تأكد_يساوي(فجوة(529), 4, "1000010001")
# apl-source:33
تأكد_يساوي(فجوة(20), 1, "10100")
# apl-source:34
تأكد_يساوي(فجوة(15), 0, "1111")
# apl-source:35
