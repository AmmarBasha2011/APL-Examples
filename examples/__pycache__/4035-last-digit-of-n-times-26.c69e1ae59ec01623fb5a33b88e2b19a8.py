
# apl-source:1
# مثال 4035 — آخر رقم من ن×26
# apl-source:2
# Last digit of n times 26
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4035-last-digit-of-n-times-26.apl
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
  return (ن * 26) % 10
# apl-source:20

# apl-source:21
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:22
تأكد_يساوي(ف(1), 6, "حالة 2")
# apl-source:23
تأكد_يساوي(ف(7), 2, "حالة 3")
# apl-source:24
تأكد_يساوي(ف(12), 2, "حالة 4")
# apl-source:25
تأكد_يساوي(ف(99), 4, "حالة 5")
# apl-source:26
