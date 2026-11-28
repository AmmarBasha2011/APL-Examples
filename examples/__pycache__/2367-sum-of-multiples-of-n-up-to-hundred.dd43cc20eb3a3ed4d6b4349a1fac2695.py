
# apl-source:1
# مثال 2367 — مجموع مضاعفات ن حتى مئة
# apl-source:2
# Sum of multiples up to 100
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2367-sum-of-multiples-of-n-up-to-hundred.apl
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
  for ي in range(ن, 101, ن):
    # apl-source:21
    م = م + ي
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(1), 5050, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(3), 1683, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(7), 735, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(10), 550, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(25), 250, "حالة 5")
# apl-source:29
تأكد_يساوي(ف(50), 150, "حالة 6")
# apl-source:30
