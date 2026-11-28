
# apl-source:1
# مثال 2125 — ترتيب العدد المثلثي
# apl-source:2
# Triangular number index
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2125-triangular-number-index-or-minus-one.apl
# apl-source:6

# apl-source:7
# # إن لم يوجد نرجع -1
# apl-source:8
# # نزيد k حتى نبلغ العدد
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
def ترتيب(ن):
  # apl-source:19
  ك = 0
  # apl-source:20
  while ك * (ك + 1) // 2 < ن:
    # apl-source:21
    ك = ك + 1
  # apl-source:22
  if ك * (ك + 1) // 2 == ن:
    # apl-source:23
    return ك
  # apl-source:24
  return -1
# apl-source:25

# apl-source:26
تأكد_يساوي(ترتيب(28), 7, "٢٨")
# apl-source:27
تأكد_يساوي(ترتيب(10), 4, "١٠")
# apl-source:28
تأكد_يساوي(ترتيب(1), 1, "١")
# apl-source:29
تأكد_يساوي(ترتيب(15), 5, "١٥")
# apl-source:30
تأكد_يساوي(ترتيب(11), -1, "١١")
# apl-source:31
