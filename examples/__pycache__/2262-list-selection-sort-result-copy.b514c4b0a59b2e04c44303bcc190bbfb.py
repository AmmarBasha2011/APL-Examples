import copy
# apl-source:1
# مثال 2262 — فرز الاختيار على نسخة
# apl-source:2
# Selection sort on copy
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2262-list-selection-sort-result-copy.apl
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
  ر = ق[:]
  # apl-source:20
  for ي in range(len(ر)):
    # apl-source:21
    م = ي
    # apl-source:22
    for ك in range(ي + 1, len(ر)):
      # apl-source:23
      if ر[ك] < ر[م]:
        # apl-source:24
        م = ك
    # apl-source:25
    ر[ي], ر[م] = ر[م], ر[ي]
  # apl-source:26
  return ر
# apl-source:27

# apl-source:28
تأكد_يساوي(ف([3, 1, 2]), [1, 2, 3], "حالة 1")
# apl-source:29
تأكد_يساوي(ف([5]), [5], "حالة 2")
# apl-source:30
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6], "حالة 3")
# apl-source:31
تأكد_يساوي(ف([-2, 0, 7, 7, 4]), [-2, 0, 4, 7, 7], "حالة 4")
# apl-source:32
تأكد_يساوي(ف([10, 20, 10, 30, 20, 10]), [10, 10, 10, 20, 20, 30], "حالة 5")
# apl-source:33
