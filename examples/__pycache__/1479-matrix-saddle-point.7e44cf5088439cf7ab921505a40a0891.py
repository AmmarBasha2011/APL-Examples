
# apl-source:1
# مثال 1479 — نقطة السرج
# apl-source:2
# Matrix saddle point
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1479-matrix-saddle-point.apl
# apl-source:6

# apl-source:7
# نأخذ أصغر عنصر في كل صف
# apl-source:8
# ثم نتأكد أنه أكبر ما في عموده
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
def نقطة_السرج(م):
  # apl-source:19
  for ص in range(len(م)):
    # apl-source:20
    صغرى = م[ص][0]
    # apl-source:21
    عمود = 0
    # apl-source:22
    for ع in range(len(م[ص])):
      # apl-source:23
      if م[ص][ع] < صغرى:
        # apl-source:24
        صغرى = م[ص][ع]
        # apl-source:25
        عمود = ع
    # apl-source:26
    أكبر_في_العمود = True
    # apl-source:27
    for ق in range(len(م)):
      # apl-source:28
      if م[ق][عمود] > صغرى:
        # apl-source:29
        أكبر_في_العمود = False
    # apl-source:30
    if أكبر_في_العمود:
      # apl-source:31
      return صغرى
  # apl-source:32
  return -1
# apl-source:33

# apl-source:34
تأكد_يساوي(نقطة_السرج([[3, 1], [1, 3]]), -1, "لا يوجد")
# apl-source:35
تأكد_يساوي(نقطة_السرج([[1, 2], [3, 4]]), 3, "يوجد")
# apl-source:36
تأكد_يساوي(نقطة_السرج([[9]]), 9, "وحيدة")
# apl-source:37
