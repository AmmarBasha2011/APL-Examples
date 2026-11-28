
# apl-source:1
# مثال 2951 — إزاحة يسار 4 مع قناع بايت
# apl-source:2
# Shift left 4 and mask byte
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2951-shift-left-by-4-then-mask-byte.apl
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
  return (ن << 4) & 255
# apl-source:20

# apl-source:21
تأكد_يساوي(ف(1), 16, "حالة 1")
# apl-source:22
تأكد_يساوي(ف(3), 48, "حالة 2")
# apl-source:23
تأكد_يساوي(ف(85), 80, "حالة 3")
# apl-source:24
تأكد_يساوي(ف(170), 160, "حالة 4")
# apl-source:25
تأكد_يساوي(ف(255), 240, "حالة 5")
# apl-source:26
