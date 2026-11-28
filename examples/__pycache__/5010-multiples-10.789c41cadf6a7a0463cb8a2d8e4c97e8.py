
# apl-source:1
# مثال 5010 — أول 8 مضاعفات للعدد 10 بدءاً من n
# apl-source:2
# Eight multiples starting at n for step 10
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5010-multiples-10.apl
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
    ر = ر + [ن + ي * 10]
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف(0), [0, 10, 20, 30, 40, 50, 60, 70], "حالة 1")
# apl-source:24
تأكد_يساوي(ف(5), [5, 15, 25, 35, 45, 55, 65, 75], "حالة 2")
# apl-source:25
تأكد_يساوي(ف(100), [100, 110, 120, 130, 140, 150, 160, 170], "حالة 3")
# apl-source:26
