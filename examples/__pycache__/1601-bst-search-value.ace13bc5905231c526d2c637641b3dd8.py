
# apl-source:1
# مثال 1601 — البحث في شجرة بحث
# apl-source:2
# Search in a binary search tree
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1601-bst-search-value.apl
# apl-source:6

# apl-source:7
# القيمة الأصغر في اليسار
# apl-source:8
# نصل إلى العقدة أو إلى الفراغ
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
def ابحث(ش, قيمة):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return False
  # apl-source:21
  if قيمة == ش[0]:
    # apl-source:22
    return True
  # apl-source:23
  if قيمة < ش[0]:
    # apl-source:24
    return ابحث(ش[1], قيمة)
  # apl-source:25
  return ابحث(ش[2], قيمة)
# apl-source:26

# apl-source:27
شجرة = [8, [3, [1, [], []], [6, [], []]], [10, [], [14, [], []]]]
# apl-source:28
تأكد_يساوي(ابحث(شجرة, 6), True, "موجود")
# apl-source:29
تأكد_يساوي(ابحث(شجرة, 7), False, "غير موجود")
# apl-source:30
تأكد_يساوي(ابحث([], 1), False, "فارغة")
# apl-source:31
