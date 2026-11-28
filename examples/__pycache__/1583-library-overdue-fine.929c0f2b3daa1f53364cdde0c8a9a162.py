
# apl-source:1
# مثال 1583 — غرامة تأخر كتاب المكتبة
# apl-source:2
# Library overdue fine
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1583-library-overdue-fine.apl
# apl-source:6

# apl-source:7
# أول سبعة أيام بسعر منخفض
# apl-source:8
# ما بعدها بسعر مضاعف
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
def غرامة_الكتاب(أيام_التأخير):
  # apl-source:19
  if أيام_التأخير <= 0:
    # apl-source:20
    return 0
  # apl-source:21
  أول = min(أيام_التأخير, 7)
  # apl-source:22
  باقي = أيام_التأخير - أول
  # apl-source:23
  return أول * 1 + باقي * 2
# apl-source:24

# apl-source:25
تأكد_يساوي(غرامة_الكتاب(0), 0, "في الموعد")
# apl-source:26
تأكد_يساوي(غرامة_الكتاب(5), 5, "خمسة أيام")
# apl-source:27
تأكد_يساوي(غرامة_الكتاب(10), 13, "عشرة أيام")
# apl-source:28
تأكد_يساوي(غرامة_الكتاب(7), 7, "أسبوع")
# apl-source:29
