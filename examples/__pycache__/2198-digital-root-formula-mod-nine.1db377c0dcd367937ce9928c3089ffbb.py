
# apl-source:1
# مثال 2198 — الجذر الرقمي بالباقي
# apl-source:2
# Digital root by mod nine
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2198-digital-root-formula-mod-nine.apl
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
    return 0
  # apl-source:21
  return 1 + (ن - 1) % 9
# apl-source:22

# apl-source:23
تأكد_يساوي(ف(0), 0, "حالة 0")
# apl-source:24
تأكد_يساوي(ف(9), 9, "حالة 9")
# apl-source:25
تأكد_يساوي(ف(38), 2, "حالة 38")
# apl-source:26
تأكد_يساوي(ف(999), 9, "حالة 999")
# apl-source:27
تأكد_يساوي(ف(12345), 6, "حالة 12345")
# apl-source:28
