
# apl-source:1
# مثال 1608 — المنظر من اليمين لشجرة
# apl-source:2
# Binary tree right side view
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1608-tree-right-side-view.apl
# apl-source:6

# apl-source:7
# نمر على المستويات
# apl-source:8
# نأخذ آخر قيمة من كل مستوى
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
def منظر_أيمن(ش):
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
    ناتج.append(حالي[len(حالي) - 1][0])
    # apl-source:25
    تالي = []
    # apl-source:26
    for ع in حالي:
      # apl-source:27
      if ع[1] != []:
        # apl-source:28
        تالي.append(ع[1])
      # apl-source:29
      if ع[2] != []:
        # apl-source:30
        تالي.append(ع[2])
    # apl-source:31
    حالي = تالي
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
تأكد_يساوي(منظر_أيمن([1, [2, [], [5, [], []]], [3, [], [4, [], []]]]), [1, 3, 4], "ثلاثة")
# apl-source:35
تأكد_يساوي(منظر_أيمن([1, [2, [], []], []]), [1, 2], "يسار فقط")
# apl-source:36
تأكد_يساوي(منظر_أيمن([]), [], "فارغة")
# apl-source:37
