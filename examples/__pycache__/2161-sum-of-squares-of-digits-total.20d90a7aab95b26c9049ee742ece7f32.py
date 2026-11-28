
# apl-source:1
# مثال 2161 — مجموع مربعات الأرقام
# apl-source:2
# Sum of squared digits
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2161-sum-of-squares-of-digits-total.apl
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
  for ر in str(ن):
    # apl-source:21
    م = م + int(ر) * int(ر)
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), 0, "حالة 0")
# apl-source:25
تأكد_يساوي(ف(5), 25, "حالة 5")
# apl-source:26
تأكد_يساوي(ف(123), 14, "حالة 123")
# apl-source:27
تأكد_يساوي(ف(9999), 324, "حالة 9999")
# apl-source:28
