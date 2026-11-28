
# apl-source:1
# مثال 1665 — أصفار نهاية المضروب
# apl-source:2
# Trailing zeros of factorial
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1665-trailing-zeros-of-factorial.apl
# apl-source:6

# apl-source:7
# كل صفر يأتي من عاملي اثنين وخمسة
# apl-source:8
# نعد مضاعفات الخمسة وقواها
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
def أصفار_المضروب(ن):
  # apl-source:19
  عد = 0
  # apl-source:20
  ق = 5
  # apl-source:21
  while ق <= ن:
    # apl-source:22
    عد = عد + ن // ق
    # apl-source:23
    ق = ق * 5
  # apl-source:24
  return عد
# apl-source:25

# apl-source:26
تأكد_يساوي(أصفار_المضروب(5), 1, "خمسة")
# apl-source:27
تأكد_يساوي(أصفار_المضروب(25), 6, "خمس وعشرون")
# apl-source:28
تأكد_يساوي(أصفار_المضروب(100), 24, "مئة")
# apl-source:29
تأكد_يساوي(أصفار_المضروب(4), 0, "أربعة")
# apl-source:30
