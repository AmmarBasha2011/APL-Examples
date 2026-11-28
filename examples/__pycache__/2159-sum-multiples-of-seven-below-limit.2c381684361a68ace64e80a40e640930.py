
# apl-source:1
# مثال 2159 — مجموع مضاعفات السبعة تحت حد
# apl-source:2
# Sum of multiples of seven below limit
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2159-sum-multiples-of-seven-below-limit.apl
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
  for ي in range(0, ن, 7):
    # apl-source:21
    م = م + ي
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(1), 0, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(8), 7, "حالة 8")
# apl-source:26
تأكد_يساوي(ف(50), 196, "حالة 50")
# apl-source:27
تأكد_يساوي(ف(100), 735, "حالة 100")
# apl-source:28
