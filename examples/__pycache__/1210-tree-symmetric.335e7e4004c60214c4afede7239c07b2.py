
# apl-source:1
# مثال 1210 — شجرة متناظرة
# apl-source:2
# Symmetric tree check
# apl-source:3
# Demonstrates: تكرار ذاتي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1210-tree-symmetric.apl
# apl-source:6

# apl-source:7
# نقارن الفرع الأيسر بالأيمن معكوساً
# apl-source:8
# القيم متساوية والأبناء متقابلون
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
def مرآة(أ, ب):
  # apl-source:19
  if (len(أ) == 0) and (len(ب) == 0):
    # apl-source:20
    return True
  # apl-source:21
  if (len(أ) == 0) or (len(ب) == 0):
    # apl-source:22
    return False
  # apl-source:23
  if أ[0] != ب[0]:
    # apl-source:24
    return False
  # apl-source:25
  س1 = مرآة(أ[1], ب[2])
  # apl-source:26
  if not س1:
    # apl-source:27
    return False
  # apl-source:28
  return مرآة(أ[2], ب[1])
# apl-source:29

# apl-source:30
def متناظرة(ش):
  # apl-source:31
  if len(ش) == 0:
    # apl-source:32
    return True
  # apl-source:33
  return مرآة(ش[1], ش[2])
# apl-source:34

# apl-source:35
سليمة = [1, [2, [3, [], []], [4, [], []]], [2, [4, [], []], [3, [], []]]]
# apl-source:36
معطوبة = [1, [2, [], [3, [], []]], [2, [], [3, [], []]]]
# apl-source:37
تأكد_يساوي(متناظرة(سليمة), True, "متناظرة")
# apl-source:38
تأكد_يساوي(متناظرة(معطوبة), False, "غير متناظرة")
# apl-source:39
تأكد_يساوي(متناظرة([]), True, "فارغة")
# apl-source:40
