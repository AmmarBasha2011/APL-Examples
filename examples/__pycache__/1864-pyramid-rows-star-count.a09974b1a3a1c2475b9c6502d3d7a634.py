
# apl-source:1
# مثال 1864 — عدد نجوم الهرم
# apl-source:2
# Total stars in a pyramid
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1864-pyramid-rows-star-count.apl
# apl-source:6

# apl-source:7
# نجمع النجوم صفاً صفاً
# apl-source:8
# المجموع مربع عدد الصفوف
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
def نجوم_الهرم(ص):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ك in range(1, ص + 1):
    # apl-source:21
    مجموع = مجموع + 2 * ك - 1
  # apl-source:22
  return مجموع
# apl-source:23

# apl-source:24
تأكد_يساوي(نجوم_الهرم(1), 1, "صف")
# apl-source:25
تأكد_يساوي(نجوم_الهرم(4), 16, "أربعة")
# apl-source:26
تأكد_يساوي(نجوم_الهرم(10), 100, "عشرة")
# apl-source:27
