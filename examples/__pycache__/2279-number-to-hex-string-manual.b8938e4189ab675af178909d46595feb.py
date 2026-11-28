
# apl-source:1
# مثال 2279 — عدد إلى سلسلة سداسية عشرية
# apl-source:2
# Number to hex string
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2279-number-to-hex-string-manual.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return "0"
  # apl-source:21
  ر = "0123456789abcdef"
  # apl-source:22
  خ = ""
  # apl-source:23
  while ن > 0:
    # apl-source:24
    خ = ر[ن % 16] + خ
    # apl-source:25
    ن = ن // 16
  # apl-source:26
  return خ
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(0), "0", "حالة 1")
# apl-source:29
تأكد_يساوي(ف(10), "a", "حالة 2")
# apl-source:30
تأكد_يساوي(ف(255), "ff", "حالة 3")
# apl-source:31
تأكد_يساوي(ف(4096), "1000", "حالة 4")
# apl-source:32
تأكد_يساوي(ف(65535), "ffff", "حالة 5")
# apl-source:33
