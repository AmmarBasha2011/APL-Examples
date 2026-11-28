
# apl-source:1
# مثال 1205 — مستويات شجرة
# apl-source:2
# Level order traversal of nested list tree
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1205-tree-level-order-list.apl
# apl-source:6

# apl-source:7
# نمر على عقد المستوى كلها
# apl-source:8
# ونجمع أبناءها للمستوى التالي
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
  ناتج = []
  # apl-source:20
  if len(ش) == 0:
    # apl-source:21
    return ناتج
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
      قيم = قيم + [ع[0]]
      # apl-source:28
      if len(ع[1]) > 0:
        # apl-source:29
        تالي = تالي + [ع[1]]
      # apl-source:30
      if len(ع[2]) > 0:
        # apl-source:31
        تالي = تالي + [ع[2]]
    # apl-source:32
    ناتج = ناتج + [قيم]
    # apl-source:33
    حالي = تالي
  # apl-source:34
  return ناتج
# apl-source:35

# apl-source:36
شجرة = [3, [9, [], []], [20, [15, [], []], [7, [], []]]]
# apl-source:37
تأكد_يساوي(مستويات(شجرة), [[3], [9, 20], [15, 7]], "ثلاثة مستويات")
# apl-source:38
تأكد_يساوي(مستويات([]), [], "فارغة")
# apl-source:39
تأكد_يساوي(مستويات([1, [], []]), [[1]], "جذر")
# apl-source:40
