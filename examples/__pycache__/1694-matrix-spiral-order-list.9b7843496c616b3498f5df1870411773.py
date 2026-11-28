
# apl-source:1
# مثال 1694 — قراءة المصفوفة حلزونياً
# apl-source:2
# Spiral order of a matrix
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1694-matrix-spiral-order-list.apl
# apl-source:6

# apl-source:7
# نضيق الحدود الأربعة
# apl-source:8
# نقرأ كل ضلع بدوره
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
  ناتج = []
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
    for ك in range(يسار, يمين + 1):
      # apl-source:26
      ناتج.append(م[أعلى][ك])
    # apl-source:27
    أعلى = أعلى + 1
    # apl-source:28
    for ك in range(أعلى, أسفل + 1):
      # apl-source:29
      ناتج.append(م[ك][يمين])
    # apl-source:30
    يمين = يمين - 1
    # apl-source:31
    if أعلى <= أسفل:
      # apl-source:32
      for ك in range(يمين, يسار - 1, -1):
        # apl-source:33
        ناتج.append(م[أسفل][ك])
      # apl-source:34
      أسفل = أسفل - 1
    # apl-source:35
    if يسار <= يمين:
      # apl-source:36
      for ك in range(أسفل, أعلى - 1, -1):
        # apl-source:37
        ناتج.append(م[ك][يسار])
      # apl-source:38
      يسار = يسار + 1
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
تأكد_يساوي(حلزوني([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5], "ثلاثة")
# apl-source:42
تأكد_يساوي(حلزوني([[1, 2], [3, 4]]), [1, 2, 4, 3], "اثنان")
# apl-source:43
تأكد_يساوي(حلزوني([[1, 2, 3]]), [1, 2, 3], "صف")
# apl-source:44
