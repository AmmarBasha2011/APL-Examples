
# apl-source:1
# مثال 2058 — الفرز بالعد لمدى صغير
# apl-source:2
# Counting sort small range
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2058-counting-sort-small-integer-range.apl
# apl-source:6

# apl-source:7
# # المدى المعروف يسمح بمصفوفة عدادات
# apl-source:8
# # التعقيد خطي
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
def افرز(ق, اقصى):
  # apl-source:19
  عدادات = [0] * (اقصى + 1)
  # apl-source:20
  for ع in ق:
    # apl-source:21
    عدادات[ع] = عدادات[ع] + 1
  # apl-source:22
  خرج = []
  # apl-source:23
  for قيمة in range(اقصى + 1):
    # apl-source:24
    خرج = خرج + [قيمة] * عدادات[قيمة]
  # apl-source:25
  return خرج
# apl-source:26

# apl-source:27
تأكد_يساوي(افرز([4, 2, 2, 8, 3, 3, 1], 9), [1, 2, 2, 3, 3, 4, 8], "سبعة")
# apl-source:28
تأكد_يساوي(افرز([], 5), [], "فارغة")
# apl-source:29
تأكد_يساوي(افرز([0, 0, 1], 1), [0, 0, 1], "صغيرة")
# apl-source:30
