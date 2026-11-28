
# apl-source:1
# مثال 5005 — أول 8 مضاعفات للعدد 9 بدءاً من n
# apl-source:2
# Eight multiples starting at n for step 9
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5005-multiples-9.apl
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
    ر = ر + [ن + ي * 9]
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف(0), [0, 9, 18, 27, 36, 45, 54, 63], "حالة 1")
# apl-source:24
تأكد_يساوي(ف(5), [5, 14, 23, 32, 41, 50, 59, 68], "حالة 2")
# apl-source:25
تأكد_يساوي(ف(100), [100, 109, 118, 127, 136, 145, 154, 163], "حالة 3")
# apl-source:26
