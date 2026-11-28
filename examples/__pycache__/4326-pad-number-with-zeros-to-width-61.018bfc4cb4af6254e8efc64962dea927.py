
# apl-source:1
# مثال 4326 — ملء الأصفار لعرض 61
# apl-source:2
# Zero pad to width 61
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4326-pad-number-with-zeros-to-width-61.apl
# apl-source:6

# apl-source:7
# # ندخل القيمة
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
  return str(ن).zfill(61)
# apl-source:20

# apl-source:21
تأكد_يساوي(ف(7), "0000000000000000000000000000000000000000000000000000000000007", "حالة 1")
# apl-source:22
تأكد_يساوي(ف(42), "0000000000000000000000000000000000000000000000000000000000042", "حالة 2")
# apl-source:23
تأكد_يساوي(ف(123), "0000000000000000000000000000000000000000000000000000000000123", "حالة 3")
# apl-source:24
تأكد_يساوي(ف(99999), "0000000000000000000000000000000000000000000000000000000099999", "حالة 4")
# apl-source:25
