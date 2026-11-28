
# apl-source:1
# مثال 3714 — مجموع قوى 49
# apl-source:2
# Sum of powers of 49
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3714-sum-of-powers-of-49-up-to-n.apl
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
  م = 0
  # apl-source:20
  for ي in range(ن + 1):
    # apl-source:21
    م = م + 49 ** ي
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), 1, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(1), 50, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(3), 120100, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(6), 14129647351, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(10), 81454605178812251, "حالة 5")
# apl-source:29
