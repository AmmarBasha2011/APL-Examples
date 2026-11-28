
# apl-source:1
# مثال 1799 — عكس ثمانية بتات
# apl-source:2
# Reverse 8 bits
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1799-reverse-bits-eight.apl
# apl-source:6

# apl-source:7
# نقرأ البت الأدنى
# apl-source:8
# ونضعه من اليمين في الناتج المزاح
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
  for ك in range(8):
    # apl-source:21
    ناتج = (ناتج << 1) | (ن & 1)
    # apl-source:22
    ن = ن >> 1
  # apl-source:23
  return ناتج
# apl-source:24

# apl-source:25
تأكد_يساوي(اعكس_بتات(1), 128, "واحد")
# apl-source:26
تأكد_يساوي(اعكس_بتات(128), 1, "128")
# apl-source:27
تأكد_يساوي(اعكس_بتات(6), 96, "ستة")
# apl-source:28
تأكد_يساوي(اعكس_بتات(255), 255, "الكل")
# apl-source:29
