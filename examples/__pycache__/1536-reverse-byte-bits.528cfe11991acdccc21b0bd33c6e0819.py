
# apl-source:1
# مثال 1536 — عكس بتات بايت
# apl-source:2
# Reverse bits of a byte
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1536-reverse-byte-bits.apl
# apl-source:6

# apl-source:7
# نأخذ البت الأدنى ونضيفه من اليمين للناتج
# apl-source:8
# نكرر ثماني مرات
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
def اعكس_بايت(ن):
  # apl-source:19
  ناتج = 0
  # apl-source:20
  for ع in range(8):
    # apl-source:21
    ناتج = (ناتج << 1) | (ن & 1)
    # apl-source:22
    ن = ن >> 1
  # apl-source:23
  return ناتج
# apl-source:24

# apl-source:25
تأكد_يساوي(اعكس_بايت(1), 128, "واحد")
# apl-source:26
تأكد_يساوي(اعكس_بايت(6), 96, "ستة")
# apl-source:27
تأكد_يساوي(اعكس_بايت(255), 255, "كامل")
# apl-source:28
تأكد_يساوي(اعكس_بايت(0), 0, "صفر")
# apl-source:29
