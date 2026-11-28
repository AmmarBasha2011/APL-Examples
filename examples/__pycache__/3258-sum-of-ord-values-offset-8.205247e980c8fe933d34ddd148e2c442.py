
# apl-source:1
# مثال 3258 — مجموع ord مع إزاحة 8
# apl-source:2
# Sum of ord values plus 8 each
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3258-sum-of-ord-values-offset-8.apl
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
    م = م + ord(ح) + 8
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
تأكد_يساوي(ف("a"), 105, "حالة 1")
# apl-source:25
تأكد_يساوي(ف("abc"), 318, "حالة 2")
# apl-source:26
تأكد_يساوي(ف("xyz"), 387, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(""), 0, "حالة 4")
# apl-source:28
