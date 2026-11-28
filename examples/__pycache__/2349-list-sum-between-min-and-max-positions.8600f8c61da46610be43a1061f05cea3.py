
# apl-source:1
# مثال 2349 — مجموع بين الأصغر والأكبر
# apl-source:2
# Sum between min and max
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2349-list-sum-between-min-and-max-positions.apl
# apl-source:6

# apl-source:7
# # نمرر القائمة
# apl-source:8
# # ونتحقق من الناتج
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
def ف(ق):
  # apl-source:19
  أ = ق.index(min(ق))
  # apl-source:20
  ب = ق.index(max(ق))
  # apl-source:21
  if أ > ب:
    # apl-source:22
    أ, ب = ب, أ
  # apl-source:23
  return sum(ق[أ:ب + 1])
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([1, 5, 3, 9, 2]), 18, "حالة 1")
# apl-source:26
تأكد_يساوي(ف([4]), 4, "حالة 2")
# apl-source:27
تأكد_يساوي(ف([9, 1]), 10, "حالة 3")
# apl-source:28
تأكد_يساوي(ف([2, 8, 5, 1]), 14, "حالة 4")
# apl-source:29
