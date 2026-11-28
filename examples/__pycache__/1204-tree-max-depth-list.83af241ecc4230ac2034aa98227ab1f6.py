
# apl-source:1
# مثال 1204 — عمق شجرة
# apl-source:2
# Binary tree depth with nested lists
# apl-source:3
# Demonstrates: تكرار ذاتي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1204-tree-max-depth-list.apl
# apl-source:6

# apl-source:7
# العقدة قائمة [قيمة, يسار, يمين] والفارغة قائمة فارغة
# apl-source:8
# العمق واحد زائد أكبر عمق للفرعين
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
def عمق(ش):
  # apl-source:19
  if len(ش) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  ي = عمق(ش[1])
  # apl-source:22
  ن = عمق(ش[2])
  # apl-source:23
  if ي > ن:
    # apl-source:24
    return ي + 1
  # apl-source:25
  return ن + 1
# apl-source:26

# apl-source:27
شجرة = [3, [9, [], []], [20, [15, [], []], [7, [], []]]]
# apl-source:28
تأكد_يساوي(عمق(شجرة), 3, "ثلاثة")
# apl-source:29
تأكد_يساوي(عمق([]), 0, "فارغة")
# apl-source:30
تأكد_يساوي(عمق([1, [], []]), 1, "جذر فقط")
# apl-source:31
تأكد_يساوي(عمق([1, [2, [3, [], []], []], []]), 3, "سلسلة")
# apl-source:32
