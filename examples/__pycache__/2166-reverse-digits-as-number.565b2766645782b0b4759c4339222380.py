
# apl-source:1
# مثال 2166 — عكس أرقام العدد كعدد
# apl-source:2
# Reverse digits as a number
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2166-reverse-digits-as-number.apl
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
  return int(str(ن)[::-1])
# apl-source:20

# apl-source:21
تأكد_يساوي(ف(12), 21, "حالة 12")
# apl-source:22
تأكد_يساوي(ف(100), 1, "حالة 100")
# apl-source:23
تأكد_يساوي(ف(4567), 7654, "حالة 4567")
# apl-source:24
تأكد_يساوي(ف(9), 9, "حالة 9")
# apl-source:25
