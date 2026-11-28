
# apl-source:1
# مثال 2167 — هل العدد متناظر
# apl-source:2
# Is number a palindrome
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2167-is-number-palindrome-digits.apl
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
  return str(ن) == str(ن)[::-1]
# apl-source:20

# apl-source:21
تأكد_يساوي(ف(1), True, "حالة 1")
# apl-source:22
تأكد_يساوي(ف(121), True, "حالة 121")
# apl-source:23
تأكد_يساوي(ف(123), False, "حالة 123")
# apl-source:24
تأكد_يساوي(ف(1221), True, "حالة 1221")
# apl-source:25
تأكد_يساوي(ف(10), False, "حالة 10")
# apl-source:26
