
# apl-source:1
# مثال 1600 — هل الشجرة بحث ثنائية
# apl-source:2
# Validate binary search tree
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1600-valid-bst-check.apl
# apl-source:6

# apl-source:7
# اليسار أصغر من الجذر واليمين أكبر
# apl-source:8
# نمرر الحدين نزولاً
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
def صالحة(ش, أدنى, أعلى):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return True
  # apl-source:21
  if ش[0] <= أدنى or ش[0] >= أعلى:
    # apl-source:22
    return False
  # apl-source:23
  return صالحة(ش[1], أدنى, ش[0]) and صالحة(ش[2], ش[0], أعلى)
# apl-source:24

# apl-source:25
def شجرة_بحث(ش):
  # apl-source:26
  return صالحة(ش, -1000000, 1000000)
# apl-source:27

# apl-source:28
تأكد_يساوي(شجرة_بحث([2, [1, [], []], [3, [], []]]), True, "صالحة")
# apl-source:29
تأكد_يساوي(شجرة_بحث([5, [1, [], []], [4, [3, [], []], [6, [], []]]]), False, "حفيد خاطئ")
# apl-source:30
تأكد_يساوي(شجرة_بحث([]), True, "فارغة")
# apl-source:31
