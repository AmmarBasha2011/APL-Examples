
# apl-source:1
# مثال 1211 — قلب شجرة
# apl-source:2
# Invert binary tree
# apl-source:3
# Demonstrates: تكرار ذاتي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1211-tree-invert.apl
# apl-source:6

# apl-source:7
# نقلب كل فرع أولاً
# apl-source:8
# ثم نبدل مكانيهما
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
def اقلب(ش):
  # apl-source:19
  if len(ش) == 0:
    # apl-source:20
    return []
  # apl-source:21
  return [ش[0], اقلب(ش[2]), اقلب(ش[1])]
# apl-source:22

# apl-source:23
شجرة = [4, [2, [1, [], []], [3, [], []]], [7, [6, [], []], [9, [], []]]]
# apl-source:24
مقلوبة = [4, [7, [9, [], []], [6, [], []]], [2, [3, [], []], [1, [], []]]]
# apl-source:25
تأكد_يساوي(اقلب(شجرة), مقلوبة, "مثال أول")
# apl-source:26
تأكد_يساوي(اقلب(اقلب(شجرة)), شجرة, "قلبان")
# apl-source:27
تأكد_يساوي(اقلب([]), [], "فارغة")
# apl-source:28
