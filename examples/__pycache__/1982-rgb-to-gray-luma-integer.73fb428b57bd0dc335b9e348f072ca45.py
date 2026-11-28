
# apl-source:1
# مثال 1982 — تحويل اللون إلى تدرج رمادي
# apl-source:2
# RGB to gray luma
# apl-source:3
# Demonstrates: ألوان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1982-rgb-to-gray-luma-integer.apl
# apl-source:6

# apl-source:7
# # العين أحساس للأخضر أكثر من الأحمر والأزرق
# apl-source:8
# # نستخدم القسمة الصحيحة
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
def رمادي(ر, ج, ب):
  # apl-source:19
  return (299 * ر + 587 * ج + 114 * ب) // 1000
# apl-source:20

# apl-source:21
تأكد_يساوي(رمادي(255, 0, 0), 76, "أحمر")
# apl-source:22
تأكد_يساوي(رمادي(0, 255, 0), 149, "أخضر")
# apl-source:23
تأكد_يساوي(رمادي(0, 0, 255), 29, "أزرق")
# apl-source:24
تأكد_يساوي(رمادي(255, 255, 255), 255, "أبيض")
# apl-source:25
تأكد_يساوي(رمادي(100, 100, 100), 100, "رمادي")
# apl-source:26
