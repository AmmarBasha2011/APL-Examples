
# apl-source:1
# مثال 2195 — عدد كاتالان
# apl-source:2
# Catalan number recurrence
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2195-catalan-number-by-recurrence.apl
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
  ك = 1
  # apl-source:20
  for ي in range(ن):
    # apl-source:21
    ك = ك * 2 * (2 * ي + 1) // (ي + 2)
  # apl-source:22
  return ك
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), 1, "حالة 0")
# apl-source:25
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:26
تأكد_يساوي(ف(4), 14, "حالة 4")
# apl-source:27
تأكد_يساوي(ف(5), 42, "حالة 5")
# apl-source:28
تأكد_يساوي(ف(10), 16796, "حالة 10")
# apl-source:29
