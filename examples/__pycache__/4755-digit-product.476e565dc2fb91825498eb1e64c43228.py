
# apl-source:1
# مثال 4755 — حاصل ضرب الأرقام
# apl-source:2
# product of digits
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4755-digit-product.apl
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
  ح = 1
  # apl-source:19
  for د in str(ن):
    # apl-source:20
    ح = ح * int(د)
  # apl-source:21
  return ح
# apl-source:22

# apl-source:23
تأكد_يساوي(ف(7), 7, "حالة 1")
# apl-source:24
تأكد_يساوي(ف(23), 6, "حالة 2")
# apl-source:25
تأكد_يساوي(ف(111), 1, "حالة 3")
# apl-source:26
تأكد_يساوي(ف(405), 0, "حالة 4")
# apl-source:27
تأكد_يساوي(ف(999), 729, "حالة 5")
# apl-source:28
