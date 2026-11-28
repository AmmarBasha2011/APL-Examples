
# apl-source:1
# مثال 1919 — اجتياز المصفوفة حلزونيا
# apl-source:2
# Traverse matrix in spiral order
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1919-matrix-spiral-order-traverse.apl
# apl-source:6

# apl-source:7
# نمشي على الحافة العليا ثم اليمنى
# apl-source:8
# نضيق الحدود بعد كل ضلع
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
def حلزوني(م):
  # apl-source:19
  خرج = []
  # apl-source:20
  أعلى = 0
  # apl-source:21
  أسفل = len(م) - 1
  # apl-source:22
  يسار = 0
  # apl-source:23
  يمين = len(م[0]) - 1
  # apl-source:24
  while أعلى <= أسفل and يسار <= يمين:
    # apl-source:25
    for ج in range(يسار, يمين + 1):
      # apl-source:26
      خرج = خرج + [م[أعلى][ج]]
    # apl-source:27
    أعلى = أعلى + 1
    # apl-source:28
    for ص in range(أعلى, أسفل + 1):
      # apl-source:29
      خرج = خرج + [م[ص][يمين]]
    # apl-source:30
    يمين = يمين - 1
    # apl-source:31
    if أعلى <= أسفل:
      # apl-source:32
      for ج in range(يمين, يسار - 1, -1):
        # apl-source:33
        خرج = خرج + [م[أسفل][ج]]
      # apl-source:34
      أسفل = أسفل - 1
    # apl-source:35
    if يسار <= يمين:
      # apl-source:36
      for ص in range(أسفل, أعلى - 1, -1):
        # apl-source:37
        خرج = خرج + [م[ص][يسار]]
      # apl-source:38
      يسار = يسار + 1
  # apl-source:39
  return خرج
# apl-source:40

# apl-source:41
تأكد_يساوي(حلزوني([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5], "٣ في ٣")
# apl-source:42
تأكد_يساوي(حلزوني([[1, 2, 3, 4]]), [1, 2, 3, 4], "صف")
# apl-source:43
تأكد_يساوي(حلزوني([[1], [2], [3]]), [1, 2, 3], "عمود")
# apl-source:44
