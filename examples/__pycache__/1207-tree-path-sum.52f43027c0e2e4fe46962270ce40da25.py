
# apl-source:1
# مثال 1207 — مجموع مسار
# apl-source:2
# Path sum root to leaf
# apl-source:3
# Demonstrates: تكرار ذاتي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1207-tree-path-sum.apl
# apl-source:6

# apl-source:7
# ننقص قيمة كل عقدة من الهدف
# apl-source:8
# وعند الورقة نتحقق أن الباقي صفر
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
def مسار(ش, هدف):
  # apl-source:19
  if len(ش) == 0:
    # apl-source:20
    return False
  # apl-source:21
  باق = هدف - ش[0]
  # apl-source:22
  if (len(ش[1]) == 0) and (len(ش[2]) == 0):
    # apl-source:23
    return باق == 0
  # apl-source:24
  return مسار(ش[1], باق) or مسار(ش[2], باق)
# apl-source:25

# apl-source:26
شجرة = [5, [4, [11, [7, [], []], [2, [], []]], []], [8, [13, [], []], [4, [], [1, [], []]]]]
# apl-source:27
تأكد_يساوي(مسار(شجرة, 22), True, "اثنان وعشرون")
# apl-source:28
تأكد_يساوي(مسار(شجرة, 26), True, "ست وعشرون")
# apl-source:29
تأكد_يساوي(مسار(شجرة, 5), False, "جذر ليس ورقة")
# apl-source:30
تأكد_يساوي(مسار([], 0), False, "فارغة")
# apl-source:31
