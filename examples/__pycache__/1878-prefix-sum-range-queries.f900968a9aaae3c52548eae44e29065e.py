
# apl-source:1
# مثال 1878 — استعلامات المجموع بمدى
# apl-source:2
# Range sum queries with prefix sums
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1878-prefix-sum-range-queries.apl
# apl-source:6

# apl-source:7
# نبني جدول التراكم
# apl-source:8
# المدى = فرق عنصرين
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
def ابن_تراكمي(ق):
  # apl-source:19
  ت = [0]
  # apl-source:20
  for ع in ق:
    # apl-source:21
    ت.append(ت[len(ت) - 1] + ع)
  # apl-source:22
  return ت
# apl-source:23

# apl-source:24
def مجموع_مدى(ت, أ, ب):
  # apl-source:25
  return ت[ب + 1] - ت[أ]
# apl-source:26

# apl-source:27
ت = ابن_تراكمي([1, 2, 3, 4, 5])
# apl-source:28
تأكد_يساوي(مجموع_مدى(ت, 0, 4), 15, "كامل")
# apl-source:29
تأكد_يساوي(مجموع_مدى(ت, 1, 3), 9, "وسط")
# apl-source:30
تأكد_يساوي(مجموع_مدى(ت, 2, 2), 3, "عنصر")
# apl-source:31
