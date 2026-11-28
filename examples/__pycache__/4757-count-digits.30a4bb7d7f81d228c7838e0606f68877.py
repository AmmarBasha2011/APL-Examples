
# apl-source:1
# مثال 4757 — عدد أرقام العدد
# apl-source:2
# number of digits
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4757-count-digits.apl
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
  return len(str(ن))
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(0), 1, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(9), 1, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(10), 2, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(12345), 5, "حالة 4")
# apl-source:24
تأكد_يساوي(ف(1000000), 7, "حالة 5")
# apl-source:25
