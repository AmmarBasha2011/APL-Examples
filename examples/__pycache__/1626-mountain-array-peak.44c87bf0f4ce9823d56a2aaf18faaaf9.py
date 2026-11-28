
# apl-source:1
# مثال 1626 — قمة مصفوفة الجبل
# apl-source:2
# Peak index of a mountain array
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1626-mountain-array-peak.apl
# apl-source:6

# apl-source:7
# إن كان التالي أكبر فالقمة يمين
# apl-source:8
# وإلا فهي هنا أو يسار
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
def قمة_الجبل(أ):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = len(أ) - 1
  # apl-source:21
  while ي < ج:
    # apl-source:22
    م = (ي + ج) // 2
    # apl-source:23
    if أ[م] < أ[م + 1]:
      # apl-source:24
      ي = م + 1
    # apl-source:25
    else:
      # apl-source:26
      ج = م
  # apl-source:27
  return ي
# apl-source:28

# apl-source:29
تأكد_يساوي(قمة_الجبل([0, 1, 0]), 1, "ثلاثة")
# apl-source:30
تأكد_يساوي(قمة_الجبل([0, 2, 5, 3, 1]), 2, "خمسة")
# apl-source:31
تأكد_يساوي(قمة_الجبل([1, 5, 9, 12, 8, 2]), 3, "ست")
# apl-source:32
