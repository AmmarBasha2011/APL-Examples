
# apl-source:1
# مثال 2164 — أكبر رقم في العدد
# apl-source:2
# Largest digit of a number
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2164-largest-digit-of-number.apl
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
  ك = 0
  # apl-source:20
  for ر in str(ن):
    # apl-source:21
    if int(ر) > ك:
      # apl-source:22
      ك = int(ر)
  # apl-source:23
  return ك
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(5), 5, "حالة 5")
# apl-source:26
تأكد_يساوي(ف(1203), 3, "حالة 1203")
# apl-source:27
تأكد_يساوي(ف(99), 9, "حالة 99")
# apl-source:28
تأكد_يساوي(ف(70001), 7, "حالة 70001")
# apl-source:29
