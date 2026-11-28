
# apl-source:1
# مثال 1457 — تبديل قيمتين بالـ XOR
# apl-source:2
# Swap two values with XOR
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1457-swap-with-xor.apl
# apl-source:6

# apl-source:7
# أو الحصرية مع نفسها تلغي القيمة
# apl-source:8
# ثلاث عمليات تكفي
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
def بدّل(أ, ب):
  # apl-source:19
  أ = أ ^ ب
  # apl-source:20
  ب = أ ^ ب
  # apl-source:21
  أ = أ ^ ب
  # apl-source:22
  return [أ, ب]
# apl-source:23

# apl-source:24
تأكد_يساوي(بدّل(3, 9), [9, 3], "عادي")
# apl-source:25
تأكد_يساوي(بدّل(5, 5), [5, 5], "متساويان")
# apl-source:26
تأكد_يساوي(بدّل(0, 7), [7, 0], "صفر")
# apl-source:27
