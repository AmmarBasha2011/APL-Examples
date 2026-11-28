
# apl-source:1
# مثال 1508 — عدد إلى سداسي عشري
# apl-source:2
# Integer to hexadecimal string
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1508-hex-digits-encode.apl
# apl-source:6

# apl-source:7
# الأرقام 10 إلى 15 تكتب a إلى f
# apl-source:8
# نقسم على 16 في كل خطوة
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
def سداسي(ن):
  # apl-source:19
  رموز = "0123456789abcdef"
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return "0"
  # apl-source:22
  ناتج = ""
  # apl-source:23
  while ن > 0:
    # apl-source:24
    ناتج = رموز[ن % 16] + ناتج
    # apl-source:25
    ن = ن // 16
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(سداسي(255), "ff", "255")
# apl-source:29
تأكد_يساوي(سداسي(16), "10", "ستة عشر")
# apl-source:30
تأكد_يساوي(سداسي(48879), "beef", "كلمة")
# apl-source:31
تأكد_يساوي(سداسي(0), "0", "صفر")
# apl-source:32
