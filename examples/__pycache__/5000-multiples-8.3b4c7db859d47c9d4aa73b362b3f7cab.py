
# apl-source:1
# مثال 5000 — أول 8 مضاعفات للعدد 8 بدءاً من n
# apl-source:2
# Eight multiples starting at n for step 8
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5000-multiples-8.apl
# apl-source:6

# apl-source:7
# نضيف الخطوة في كل مرة
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
  ر = []
  # apl-source:19
  for ي in range(8):
    # apl-source:20
    ر = ر + [ن + ي * 8]
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف(0), [0, 8, 16, 24, 32, 40, 48, 56], "حالة 1")
# apl-source:24
تأكد_يساوي(ف(5), [5, 13, 21, 29, 37, 45, 53, 61], "حالة 2")
# apl-source:25
تأكد_يساوي(ف(100), [100, 108, 116, 124, 132, 140, 148, 156], "حالة 3")
# apl-source:26
