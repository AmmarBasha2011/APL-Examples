
# apl-source:1
# مثال 1648 — العدد المثلثي
# apl-source:2
# Triangular number check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1648-triangular-number-check.apl
# apl-source:6

# apl-source:7
# نضيف ك تباعاً
# apl-source:8
# نتوقف حين يبلغ المجموع العدد أو يتجاوزه
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
def مثلثي(ن):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  ك = 0
  # apl-source:21
  while مجموع < ن:
    # apl-source:22
    ك = ك + 1
    # apl-source:23
    مجموع = مجموع + ك
  # apl-source:24
  return مجموع == ن
# apl-source:25

# apl-source:26
تأكد_يساوي(مثلثي(6), True, "ستة")
# apl-source:27
تأكد_يساوي(مثلثي(10), True, "عشرة")
# apl-source:28
تأكد_يساوي(مثلثي(8), False, "ثمانية")
# apl-source:29
تأكد_يساوي(مثلثي(1), True, "واحد")
# apl-source:30
