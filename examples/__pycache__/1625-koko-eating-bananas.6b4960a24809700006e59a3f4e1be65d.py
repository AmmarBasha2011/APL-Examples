
# apl-source:1
# مثال 1625 — سرعة أكل الموز
# apl-source:2
# Koko eating bananas
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1625-koko-eating-bananas.apl
# apl-source:6

# apl-source:7
# نبحث عن السرعة بين 1 وأكبر كومة
# apl-source:8
# نحسب الساعات بالتقريب لأعلى
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
def ساعات_الأكل(أكوام, سرعة):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ك in أكوام:
    # apl-source:21
    مجموع = مجموع + (ك + سرعة - 1) // سرعة
  # apl-source:22
  return مجموع
# apl-source:23

# apl-source:24
def أقل_سرعة(أكوام, ساعات):
  # apl-source:25
  ي = 1
  # apl-source:26
  ج = 1
  # apl-source:27
  for ك in أكوام:
    # apl-source:28
    if ك > ج:
      # apl-source:29
      ج = ك
  # apl-source:30
  while ي < ج:
    # apl-source:31
    م = (ي + ج) // 2
    # apl-source:32
    if ساعات_الأكل(أكوام, م) <= ساعات:
      # apl-source:33
      ج = م
    # apl-source:34
    else:
      # apl-source:35
      ي = م + 1
  # apl-source:36
  return ي
# apl-source:37

# apl-source:38
تأكد_يساوي(أقل_سرعة([3, 6, 7, 11], 8), 4, "أربع")
# apl-source:39
تأكد_يساوي(أقل_سرعة([30, 11, 23, 4, 20], 5), 30, "ثلاثون")
# apl-source:40
تأكد_يساوي(أقل_سرعة([30, 11, 23, 4, 20], 6), 23, "ثلاث وعشرون")
# apl-source:41
