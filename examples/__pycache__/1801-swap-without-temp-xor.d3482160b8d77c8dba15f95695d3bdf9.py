
# apl-source:1
# مثال 1801 — تبديل بلا متغير مؤقت
# apl-source:2
# Swap two numbers with XOR
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1801-swap-without-temp-xor.apl
# apl-source:6

# apl-source:7
# أ ^= ب ثم ب ^= أ ثم أ ^= ب
# apl-source:8
# النتيجة تبديل كامل
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
def بدّل_زوج(أ, ب):
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
تأكد_يساوي(بدّل_زوج(3, 9), [9, 3], "عددان")
# apl-source:25
تأكد_يساوي(بدّل_زوج(5, 5), [5, 5], "متساويان")
# apl-source:26
تأكد_يساوي(بدّل_زوج(0, 7), [7, 0], "صفر")
# apl-source:27
