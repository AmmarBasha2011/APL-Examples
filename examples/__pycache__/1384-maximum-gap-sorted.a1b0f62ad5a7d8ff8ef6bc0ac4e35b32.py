
# apl-source:1
# مثال 1384 — أكبر فجوة
# apl-source:2
# Maximum gap between sorted neighbors
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1384-maximum-gap-sorted.apl
# apl-source:6

# apl-source:7
# نرتب المصفوفة
# apl-source:8
# ونقارن كل عنصر مع سابقه
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
def اكبر_فجوة(أرقام):
  # apl-source:19
  if len(أرقام) < 2:
    # apl-source:20
    return 0
  # apl-source:21
  ر = sorted(أرقام)
  # apl-source:22
  اقصى = 0
  # apl-source:23
  for ع in range(1, len(ر)):
    # apl-source:24
    if ر[ع] - ر[ع - 1] > اقصى:
      # apl-source:25
      اقصى = ر[ع] - ر[ع - 1]
  # apl-source:26
  return اقصى
# apl-source:27

# apl-source:28
تأكد_يساوي(اكبر_فجوة([3,6,9,1]), 3, "ثلاثة")
# apl-source:29
تأكد_يساوي(اكبر_فجوة([10]), 0, "عنصر")
# apl-source:30
تأكد_يساوي(اكبر_فجوة([1,1,1,1]), 0, "متساوية")
# apl-source:31
