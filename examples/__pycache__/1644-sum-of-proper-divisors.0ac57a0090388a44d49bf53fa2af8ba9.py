
# apl-source:1
# مثال 1644 — مجموع القواسم الفعلية
# apl-source:2
# Sum of proper divisors
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1644-sum-of-proper-divisors.apl
# apl-source:6

# apl-source:7
# نبحث حتى الجذر التربيعي
# apl-source:8
# كل قاسم له قرين
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
def مجموع_القواسم(ن):
  # apl-source:19
  if ن == 1:
    # apl-source:20
    return 0
  # apl-source:21
  مجموع = 1
  # apl-source:22
  ك = 2
  # apl-source:23
  while ك * ك <= ن:
    # apl-source:24
    if ن % ك == 0:
      # apl-source:25
      مجموع = مجموع + ك
      # apl-source:26
      if ك != ن // ك:
        # apl-source:27
        مجموع = مجموع + ن // ك
    # apl-source:28
    ك = ك + 1
  # apl-source:29
  return مجموع
# apl-source:30

# apl-source:31
تأكد_يساوي(مجموع_القواسم(1), 0, "واحد")
# apl-source:32
تأكد_يساوي(مجموع_القواسم(6), 6, "تام")
# apl-source:33
تأكد_يساوي(مجموع_القواسم(12), 16, "وافر")
# apl-source:34
تأكد_يساوي(مجموع_القواسم(16), 15, "مربع")
# apl-source:35
