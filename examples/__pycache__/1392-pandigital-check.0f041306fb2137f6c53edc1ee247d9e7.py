
# apl-source:1
# مثال 1392 — عدد شامل الأرقام
# apl-source:2
# Pandigital number check
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1392-pandigital-check.apl
# apl-source:6

# apl-source:7
# الطول يجب أن يساوي ن
# apl-source:8
# وكل رقم يظهر بالضبط مرة
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
def شامل(نص_, ن):
  # apl-source:19
  if len(نص_) != ن:
    # apl-source:20
    return False
  # apl-source:21
  for د in range(1, ن + 1):
    # apl-source:22
    if نص_.count(str(د)) != 1:
      # apl-source:23
      return False
  # apl-source:24
  return True
# apl-source:25

# apl-source:26
تأكد_يساوي(شامل("123456789", 9), True, "تسعة")
# apl-source:27
تأكد_يساوي(شامل("52314", 5), True, "خمسة")
# apl-source:28
تأكد_يساوي(شامل("12345678", 9), False, "ناقص")
# apl-source:29
تأكد_يساوي(شامل("1123", 3), False, "تكرار")
# apl-source:30
