
# apl-source:1
# مثال 1557 — مساحة المعين بالقطرين
# apl-source:2
# Rhombus area from diagonals
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1557-rhombus-area-diagonals.apl
# apl-source:6

# apl-source:7
# القطران متعامدان
# apl-source:8
# المساحة = ق1 × ق2 ÷ 2
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
def مساحة_المعين(ق1, ق2):
  # apl-source:19
  return ق1 * ق2 / 2
# apl-source:20

# apl-source:21
تأكد_يساوي(مساحة_المعين(6, 8), 24.0, "عادي")
# apl-source:22
تأكد_يساوي(مساحة_المعين(10, 10), 50.0, "مربع")
# apl-source:23
تأكد_يساوي(مساحة_المعين(0, 5), 0.0, "منحل")
# apl-source:24
