
# apl-source:1
# مثال 4754 — الجذر الرقمي
# apl-source:2
# digital root
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4754-digital-root.apl
# apl-source:6

# apl-source:7
# نحوّل العدد لنص ونمر على أرقامه
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
  while ن >= 10:
    # apl-source:19
    ج = 0
    # apl-source:20
    for د in str(ن):
      # apl-source:21
      ج = ج + int(د)
    # apl-source:22
    ن = ج
  # apl-source:23
  return ن
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:26
تأكد_يساوي(ف(9), 9, "حالة 2")
# apl-source:27
تأكد_يساوي(ف(38), 2, "حالة 3")
# apl-source:28
تأكد_يساوي(ف(999), 9, "حالة 4")
# apl-source:29
تأكد_يساوي(ف(12345), 6, "حالة 5")
# apl-source:30
