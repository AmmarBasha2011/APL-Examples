
# apl-source:1
# مثال 1491 — عمق القوائم المتداخلة
# apl-source:2
# Nested list depth
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1491-nested-list-depth.apl
# apl-source:6

# apl-source:7
# القائمة الفارغة عمقها واحد
# apl-source:8
# العمق واحد زائد أكبر عمق لعناصرها
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
def العمق(ق):
  # apl-source:19
  أقصى = 0
  # apl-source:20
  for ع in ق:
    # apl-source:21
    if type(ع) == type([]):
      # apl-source:22
      د = العمق(ع)
      # apl-source:23
      if د > أقصى:
        # apl-source:24
        أقصى = د
  # apl-source:25
  return أقصى + 1
# apl-source:26

# apl-source:27
تأكد_يساوي(العمق([1, 2, 3]), 1, "مسطحة")
# apl-source:28
تأكد_يساوي(العمق([1, [2, [3]]]), 3, "ثلاثة مستويات")
# apl-source:29
تأكد_يساوي(العمق([]), 1, "فارغة")
# apl-source:30
