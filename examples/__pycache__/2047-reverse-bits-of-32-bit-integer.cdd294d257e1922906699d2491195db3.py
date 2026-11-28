
# apl-source:1
# مثال 2047 — عكس بتات عدد من 32 بت
# apl-source:2
# Reverse 32-bit integer bits
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2047-reverse-bits-of-32-bit-integer.apl
# apl-source:6

# apl-source:7
# # ندفع الناتج لليسار ونضيف آخر بت
# apl-source:8
# # ثم نزيح العدد لليمين
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
def اعكس_بتات(ن):
  # apl-source:19
  ناتج = 0
  # apl-source:20
  for ك in range(32):
    # apl-source:21
    ناتج = (ناتج << 1) | (ن & 1)
    # apl-source:22
    ن = ن >> 1
  # apl-source:23
  return ناتج
# apl-source:24

# apl-source:25
تأكد_يساوي(اعكس_بتات(43261596), 964176192, "كلاسيكي")
# apl-source:26
تأكد_يساوي(اعكس_بتات(1), 2147483648, "واحد")
# apl-source:27
تأكد_يساوي(اعكس_بتات(0), 0, "صفر")
# apl-source:28
