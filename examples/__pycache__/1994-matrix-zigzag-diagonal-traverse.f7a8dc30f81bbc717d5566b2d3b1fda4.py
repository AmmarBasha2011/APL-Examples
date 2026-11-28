
# apl-source:1
# مثال 1994 — مرور قطري متعرج على المصفوفة
# apl-source:2
# Zigzag diagonal matrix traversal
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1994-matrix-zigzag-diagonal-traverse.apl
# apl-source:6

# apl-source:7
# # خلايا القطر s يكون فيها i+j يساوي s
# apl-source:8
# # الأقطار الزوجية نقرأها من الأسفل للأعلى
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
def متعرج(م):
  # apl-source:19
  ص = len(م)
  # apl-source:20
  if ص == 0:
    # apl-source:21
    return []
  # apl-source:22
  ع = len(م[0])
  # apl-source:23
  خرج = []
  # apl-source:24
  for س in range(ص + ع - 1):
    # apl-source:25
    قطر = []
    # apl-source:26
    for ي in range(max(0, س - ع + 1), min(س, ص - 1) + 1):
      # apl-source:27
      قطر = قطر + [م[ي][س - ي]]
    # apl-source:28
    if س % 2 == 0:
      # apl-source:29
      قطر.reverse()
    # apl-source:30
    خرج = خرج + قطر
  # apl-source:31
  return خرج
# apl-source:32

# apl-source:33
تأكد_يساوي(متعرج([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 4, 7, 5, 3, 6, 8, 9], "٣×٣")
# apl-source:34
تأكد_يساوي(متعرج([[1, 2], [3, 4]]), [1, 2, 3, 4], "٢×٢")
# apl-source:35
تأكد_يساوي(متعرج([[1, 2, 3]]), [1, 2, 3], "صف واحد")
# apl-source:36
