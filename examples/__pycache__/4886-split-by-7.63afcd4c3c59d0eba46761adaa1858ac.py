
# apl-source:1
# مثال 4886 — تقسيم القيمة على 7 إلى (خارج, باقي)
# apl-source:2
# Split into quotient and remainder by 7
# apl-source:3
# Demonstrates: مالية وهندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4886-split-by-7.apl
# apl-source:6

# apl-source:7
# نستخدم // و %
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
  return [ن // 7, ن % 7]
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(0), [0, 0], "حالة 1")
# apl-source:21
تأكد_يساوي(ف(6), [0, 6], "حالة 2")
# apl-source:22
تأكد_يساوي(ف(7), [1, 0], "حالة 3")
# apl-source:23
تأكد_يساوي(ف(1000), [142, 6], "حالة 4")
# apl-source:24
تأكد_يساوي(ف(12345), [1763, 4], "حالة 5")
# apl-source:25
