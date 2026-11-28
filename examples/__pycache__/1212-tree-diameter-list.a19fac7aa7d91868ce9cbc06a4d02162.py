
# apl-source:1
# مثال 1212 — قطر شجرة
# apl-source:2
# Diameter of binary tree
# apl-source:3
# Demonstrates: تكرار ذاتي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1212-tree-diameter-list.apl
# apl-source:6

# apl-source:7
# نحسب عمق كل فرع عند كل عقدة
# apl-source:8
# وأطول مسار يمر بها هو مجموع عمقي فرعيها
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
def عمق_وقطر(ش):
  # apl-source:19
  if len(ش) == 0:
    # apl-source:20
    return [0, 0]
  # apl-source:21
  ي = عمق_وقطر(ش[1])
  # apl-source:22
  ن = عمق_وقطر(ش[2])
  # apl-source:23
  عمق_ = 1 + max(ي[0], ن[0])
  # apl-source:24
  قطر_ = max(ي[0] + ن[0], max(ي[1], ن[1]))
  # apl-source:25
  return [عمق_, قطر_]
# apl-source:26

# apl-source:27
شجرة = [1, [2, [4, [], []], [5, [], []]], [3, [], []]]
# apl-source:28
تأكد_يساوي(عمق_وقطر(شجرة)[1], 3, "ثلاثة")
# apl-source:29
تأكد_يساوي(عمق_وقطر([1, [2, [], []], []])[1], 1, "واحد")
# apl-source:30
تأكد_يساوي(عمق_وقطر([])[1], 0, "فارغة")
# apl-source:31
