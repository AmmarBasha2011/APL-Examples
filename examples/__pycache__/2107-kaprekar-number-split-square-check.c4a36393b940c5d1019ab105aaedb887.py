
# apl-source:1
# مثال 2107 — أعداد كابريكار بتقسيم المربع
# apl-source:2
# Kaprekar number split check
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2107-kaprekar-number-split-square-check.apl
# apl-source:6

# apl-source:7
# # الجزء الأيمن لا يكون صفرا
# apl-source:8
# # والعدد 1 حالة خاصة
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
def كابريكار(ن):
  # apl-source:19
  if ن == 1:
    # apl-source:20
    return True
  # apl-source:21
  م = str(ن * ن)
  # apl-source:22
  for ك in range(1, len(م)):
    # apl-source:23
    ي = int(م[:ك])
    # apl-source:24
    ل = int(م[ك:])
    # apl-source:25
    if ل > 0 and ي + ل == ن:
      # apl-source:26
      return True
  # apl-source:27
  return False
# apl-source:28

# apl-source:29
تأكد_يساوي(كابريكار(9), True, "٩")
# apl-source:30
تأكد_يساوي(كابريكار(45), True, "٤٥")
# apl-source:31
تأكد_يساوي(كابريكار(297), True, "٢٩٧")
# apl-source:32
تأكد_يساوي(كابريكار(10), False, "١٠")
# apl-source:33
تأكد_يساوي(كابريكار(1), True, "١")
# apl-source:34
