
# apl-source:1
# مثال 1206 — قراءة متعرجة
# apl-source:2
# Zigzag level order
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1206-tree-zigzag-order.apl
# apl-source:6

# apl-source:7
# المستوى الأول من اليسار والثاني من اليمين وهكذا
# apl-source:8
# نعكس المستويات الفردية
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
def متعرج(ش):
  # apl-source:19
  ناتج = []
  # apl-source:20
  if len(ش) == 0:
    # apl-source:21
    return ناتج
  # apl-source:22
  حالي = [ش]
  # apl-source:23
  اتجاه = 0
  # apl-source:24
  while len(حالي) > 0:
    # apl-source:25
    قيم = []
    # apl-source:26
    تالي = []
    # apl-source:27
    for ع in حالي:
      # apl-source:28
      قيم = قيم + [ع[0]]
      # apl-source:29
      if len(ع[1]) > 0:
        # apl-source:30
        تالي = تالي + [ع[1]]
      # apl-source:31
      if len(ع[2]) > 0:
        # apl-source:32
        تالي = تالي + [ع[2]]
    # apl-source:33
    if اتجاه == 1:
      # apl-source:34
      قيم.reverse()
    # apl-source:35
    ناتج = ناتج + [قيم]
    # apl-source:36
    اتجاه = 1 - اتجاه
    # apl-source:37
    حالي = تالي
  # apl-source:38
  return ناتج
# apl-source:39

# apl-source:40
شجرة = [3, [9, [], []], [20, [15, [], []], [7, [], []]]]
# apl-source:41
تأكد_يساوي(متعرج(شجرة), [[3], [20, 9], [15, 7]], "مثال أول")
# apl-source:42
تأكد_يساوي(متعرج([]), [], "فارغة")
# apl-source:43
