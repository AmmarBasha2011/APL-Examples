
# apl-source:1
# مثال 2109 — العدد كمجموع مربعين
# apl-source:2
# Sum of two squares check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2109-sum-of-two-squares-representable.apl
# apl-source:6

# apl-source:7
# # نبحث عن a وb يحققان a²+b² = n
# apl-source:8
# # الصفر مسموح
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
def مربعين(ن):
  # apl-source:19
  ا = 0
  # apl-source:20
  while ا * ا <= ن:
    # apl-source:21
    ب = ا
    # apl-source:22
    while ا * ا + ب * ب <= ن:
      # apl-source:23
      if ا * ا + ب * ب == ن:
        # apl-source:24
        return True
      # apl-source:25
      ب = ب + 1
    # apl-source:26
    ا = ا + 1
  # apl-source:27
  return False
# apl-source:28

# apl-source:29
تأكد_يساوي(مربعين(5), True, "٥")
# apl-source:30
تأكد_يساوي(مربعين(3), False, "٣")
# apl-source:31
تأكد_يساوي(مربعين(25), True, "٢٥")
# apl-source:32
تأكد_يساوي(مربعين(0), True, "صفر")
# apl-source:33
تأكد_يساوي(مربعين(50), True, "٥٠")
# apl-source:34
تأكد_يساوي(مربعين(7), False, "٧")
# apl-source:35
