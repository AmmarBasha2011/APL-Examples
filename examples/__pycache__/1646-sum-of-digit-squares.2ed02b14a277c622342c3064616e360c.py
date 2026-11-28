
# apl-source:1
# مثال 1646 — مجموع مربعات الأرقام
# apl-source:2
# Sum of squares of digits
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1646-sum-of-digit-squares.apl
# apl-source:6

# apl-source:7
# نفصل الرقم الأخير بالباقي
# apl-source:8
# ونحذفه بالقسمة
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
def مربعات_الأرقام(ن):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  while ن > 0:
    # apl-source:21
    ر = ن % 10
    # apl-source:22
    مجموع = مجموع + ر * ر
    # apl-source:23
    ن = ن // 10
  # apl-source:24
  return مجموع
# apl-source:25

# apl-source:26
تأكد_يساوي(مربعات_الأرقام(123), 14, "ثلاثة أرقام")
# apl-source:27
تأكد_يساوي(مربعات_الأرقام(0), 0, "صفر")
# apl-source:28
تأكد_يساوي(مربعات_الأرقام(99), 162, "تسعتان")
# apl-source:29
