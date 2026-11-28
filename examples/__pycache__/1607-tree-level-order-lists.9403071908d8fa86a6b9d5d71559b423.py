
# apl-source:1
# مثال 1607 — مستويات الشجرة
# apl-source:2
# Binary tree level order
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1607-tree-level-order-lists.apl
# apl-source:6

# apl-source:7
# نعالج مستوى كاملاً في كل جولة
# apl-source:8
# نجمع أبناء المستوى للتالي
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
def مستويات(ش):
  # apl-source:19
  if ش == []:
    # apl-source:20
    return []
  # apl-source:21
  ناتج = []
  # apl-source:22
  حالي = [ش]
  # apl-source:23
  while len(حالي) > 0:
    # apl-source:24
    قيم = []
    # apl-source:25
    تالي = []
    # apl-source:26
    for ع in حالي:
      # apl-source:27
      قيم.append(ع[0])
      # apl-source:28
      if ع[1] != []:
        # apl-source:29
        تالي.append(ع[1])
      # apl-source:30
      if ع[2] != []:
        # apl-source:31
        تالي.append(ع[2])
    # apl-source:32
    ناتج.append(قيم)
    # apl-source:33
    حالي = تالي
  # apl-source:34
  return ناتج
# apl-source:35

# apl-source:36
تأكد_يساوي(مستويات([3, [9, [], []], [20, [15, [], []], [7, [], []]]]), [[3], [9, 20], [15, 7]], "ثلاثة مستويات")
# apl-source:37
تأكد_يساوي(مستويات([]), [], "فارغة")
# apl-source:38
تأكد_يساوي(مستويات([1, [], []]), [[1]], "جذر")
# apl-source:39
