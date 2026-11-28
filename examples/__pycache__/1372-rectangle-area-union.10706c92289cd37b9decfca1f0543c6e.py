
# apl-source:1
# مثال 1372 — مساحة اتحاد مستطيلين
# apl-source:2
# Total area of two rectangles
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1372-rectangle-area-union.apl
# apl-source:6

# apl-source:7
# نجمع المساحتين
# apl-source:8
# ونطرح مساحة التداخل مرة واحدة
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
def مساحة_الاتحاد(أ1, ب1, أ2, ب2, ج1, د1, ج2, د2):
  # apl-source:19
  مساحة_الاول = (أ2 - أ1) * (ب2 - ب1)
  # apl-source:20
  مساحة_الثاني = (ج2 - ج1) * (د2 - د1)
  # apl-source:21
  عرض = min(أ2, ج2) - max(أ1, ج1)
  # apl-source:22
  ارتفاع = min(ب2, د2) - max(ب1, د1)
  # apl-source:23
  تداخل = 0
  # apl-source:24
  if (عرض > 0) and (ارتفاع > 0):
    # apl-source:25
    تداخل = عرض * ارتفاع
  # apl-source:26
  return مساحة_الاول + مساحة_الثاني - تداخل
# apl-source:27

# apl-source:28
تأكد_يساوي(مساحة_الاتحاد(-3, 0, 3, 4, 0, -1, 9, 2), 45, "تداخل جزئي")
# apl-source:29
تأكد_يساوي(مساحة_الاتحاد(-2, -2, 2, 2, -2, -2, 2, 2), 16, "متطابقان")
# apl-source:30
تأكد_يساوي(مساحة_الاتحاد(0, 0, 1, 1, 2, 2, 3, 3), 2, "منفصلان")
# apl-source:31
