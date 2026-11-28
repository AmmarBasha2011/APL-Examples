
# apl-source:1
# مثال 1767 — الأيام بين سنتين
# apl-source:2
# Days between two years
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1767-date-days-between-years-simple.apl
# apl-source:6

# apl-source:7
# السنة الكبيسة 366 يوماً
# apl-source:8
# نجمع من السنة الأولى حتى ما قبل الثانية
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
def كبيسة(س):
  # apl-source:19
  if س % 400 == 0:
    # apl-source:20
    return True
  # apl-source:21
  if س % 100 == 0:
    # apl-source:22
    return False
  # apl-source:23
  return س % 4 == 0
# apl-source:24

# apl-source:25
def أيام_بين(أ, ب):
  # apl-source:26
  مجموع = 0
  # apl-source:27
  for س in range(أ, ب):
    # apl-source:28
    if كبيسة(س):
      # apl-source:29
      مجموع = مجموع + 366
    # apl-source:30
    else:
      # apl-source:31
      مجموع = مجموع + 365
  # apl-source:32
  return مجموع
# apl-source:33

# apl-source:34
تأكد_يساوي(أيام_بين(2023, 2024), 365, "عادية")
# apl-source:35
تأكد_يساوي(أيام_بين(2024, 2025), 366, "كبيسة")
# apl-source:36
تأكد_يساوي(أيام_بين(2000, 2004), 1461, "أربع")
# apl-source:37
