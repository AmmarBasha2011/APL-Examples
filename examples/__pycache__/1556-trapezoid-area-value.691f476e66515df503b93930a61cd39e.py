
# apl-source:1
# مثال 1556 — مساحة شبه المنحرف
# apl-source:2
# Trapezoid area
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1556-trapezoid-area-value.apl
# apl-source:6

# apl-source:7
# نجمع القاعدتين
# apl-source:8
# نضرب في الارتفاع ونقسم على اثنين
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
def مساحة_شبه_المنحرف(أ, ب, ارتفاع):
  # apl-source:19
  return (أ + ب) * ارتفاع / 2
# apl-source:20

# apl-source:21
تأكد_يساوي(مساحة_شبه_المنحرف(4, 6, 5), 25.0, "عادي")
# apl-source:22
تأكد_يساوي(مساحة_شبه_المنحرف(3, 3, 4), 12.0, "مستطيل")
# apl-source:23
تأكد_يساوي(مساحة_شبه_المنحرف(0, 8, 3), 12.0, "مثلث")
# apl-source:24
