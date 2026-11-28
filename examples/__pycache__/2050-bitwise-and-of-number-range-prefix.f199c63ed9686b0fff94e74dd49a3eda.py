
# apl-source:1
# مثال 2050 — AND لكل الأعداد في مدى
# apl-source:2
# Bitwise AND of range
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2050-bitwise-and-of-number-range-prefix.apl
# apl-source:6

# apl-source:7
# # نزيح الطرفين حتى يتساويا
# apl-source:8
# # ثم نعيد الإزاحة
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
def نطاق_و(ا, ب):
  # apl-source:19
  ازاحة = 0
  # apl-source:20
  while ا != ب:
    # apl-source:21
    ا = ا >> 1
    # apl-source:22
    ب = ب >> 1
    # apl-source:23
    ازاحة = ازاحة + 1
  # apl-source:24
  return ا << ازاحة
# apl-source:25

# apl-source:26
تأكد_يساوي(نطاق_و(5, 7), 4, "٥ إلى ٧")
# apl-source:27
تأكد_يساوي(نطاق_و(0, 0), 0, "صفر")
# apl-source:28
تأكد_يساوي(نطاق_و(1, 2147483647), 0, "كبير")
# apl-source:29
