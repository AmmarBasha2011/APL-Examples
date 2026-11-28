
# apl-source:1
# مثال 2316 — مجموع الأرقام داخل نص مختلط
# apl-source:2
# Sum digits in mixed text
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2316-digits-to-sum-from-text-mixed.apl
# apl-source:6

# apl-source:7
# # ندخل النص
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
  م = 0
  # apl-source:20
  for ح in ن:
    # apl-source:21
    if ح.isdigit():
      # apl-source:22
      م = م + int(ح)
  # apl-source:23
  return م
# apl-source:24

# apl-source:25
تأكد_يساوي(ف("a1b2c3"), 6, "حالة 1")
# apl-source:26
تأكد_يساوي(ف("abc"), 0, "حالة 2")
# apl-source:27
تأكد_يساوي(ف("99"), 18, "حالة 3")
# apl-source:28
تأكد_يساوي(ف("x9y9z9"), 27, "حالة 4")
# apl-source:29
