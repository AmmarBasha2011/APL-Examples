
# apl-source:1
# مثال 4777 — عدد البتات المضيئة
# apl-source:2
# Count set bits
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4777-popcount.apl
# apl-source:6

# apl-source:7
# نفحص كل بت
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
  ع = 0
  # apl-source:19
  while ن > 0:
    # apl-source:20
    ع = ع + (ن & 1)
    # apl-source:21
    ن = ن >> 1
  # apl-source:22
  return ع
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(1), 1, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(7), 3, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(255), 8, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(1024), 1, "حالة 5")
# apl-source:29
