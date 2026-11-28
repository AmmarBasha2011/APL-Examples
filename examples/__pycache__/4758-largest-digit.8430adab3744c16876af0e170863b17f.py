
# apl-source:1
# مثال 4758 — أكبر رقم في العدد
# apl-source:2
# largest digit
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4758-largest-digit.apl
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
  م = 0
  # apl-source:19
  for د in str(ن):
    # apl-source:20
    if int(د) > م:
      # apl-source:21
      م = int(د)
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(5), 5, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(120), 2, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(9081), 9, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(3333), 3, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(70419), 9, "حالة 5")
# apl-source:29
