
# apl-source:1
# مثال 1149 — مجموع مربعين
# apl-source:2
# Sum of two squares
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1149-sum-of-squares.apl
# apl-source:6

# apl-source:7
# نبدأ بمؤشرين من الصفر والجذر
# apl-source:8
# ونحرك أحدهما حسب المقارنة
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
def مجموع_مربعين(ن):
  # apl-source:19
  أ = 0
  # apl-source:20
  ب = int(ن ** 0.5)
  # apl-source:21
  while أ <= ب:
    # apl-source:22
    س = أ * أ + ب * ب
    # apl-source:23
    if س == ن:
      # apl-source:24
      return True
    # apl-source:25
    elif س < ن:
      # apl-source:26
      أ = أ + 1
    # apl-source:27
    else:
      # apl-source:28
      ب = ب - 1
  # apl-source:29
  return False
# apl-source:30

# apl-source:31
تأكد_يساوي(مجموع_مربعين(5), True, "خمسة")
# apl-source:32
تأكد_يساوي(مجموع_مربعين(3), False, "ثلاثة")
# apl-source:33
تأكد_يساوي(مجموع_مربعين(0), True, "صفر")
# apl-source:34
تأكد_يساوي(مجموع_مربعين(25), True, "خمسة وعشرون")
# apl-source:35
تأكد_يساوي(مجموع_مربعين(21), False, "واحد وعشرون")
# apl-source:36
