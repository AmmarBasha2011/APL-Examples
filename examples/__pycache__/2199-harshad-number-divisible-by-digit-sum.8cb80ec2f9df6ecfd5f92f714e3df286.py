
# apl-source:1
# مثال 2199 — عدد هارشاد
# apl-source:2
# Harshad number
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2199-harshad-number-divisible-by-digit-sum.apl
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
    م = م + int(ر)
  # apl-source:22
  return ن % م == 0
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(18), True, "حالة 18")
# apl-source:25
تأكد_يساوي(ف(19), False, "حالة 19")
# apl-source:26
تأكد_يساوي(ف(21), True, "حالة 21")
# apl-source:27
تأكد_يساوي(ف(100), True, "حالة 100")
# apl-source:28
تأكد_يساوي(ف(111), True, "حالة 111")
# apl-source:29
تأكد_يساوي(ف(12), True, "حالة 12")
# apl-source:30
