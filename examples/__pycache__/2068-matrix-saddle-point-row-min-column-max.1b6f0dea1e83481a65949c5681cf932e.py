
# apl-source:1
# مثال 2068 — نقطة السرج في مصفوفة
# apl-source:2
# Matrix saddle point
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2068-matrix-saddle-point-row-min-column-max.apl
# apl-source:6

# apl-source:7
# # نبحث عن أصغر قيمة في كل صف
# apl-source:8
# # ونتأكد أنها الأكبر في عمودها
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
def سرج(م):
  # apl-source:19
  for ي in range(len(م)):
    # apl-source:20
    ص = 0
    # apl-source:21
    for ك in range(len(م[ي])):
      # apl-source:22
      if م[ي][ك] < م[ي][ص]:
        # apl-source:23
        ص = ك
    # apl-source:24
    اكبر_عمود = True
    # apl-source:25
    for ر in range(len(م)):
      # apl-source:26
      if م[ر][ص] > م[ي][ص]:
        # apl-source:27
        اكبر_عمود = False
    # apl-source:28
    if اكبر_عمود:
      # apl-source:29
      return [ي, ص]
  # apl-source:30
  return []
# apl-source:31

# apl-source:32
تأكد_يساوي(سرج([[9, 8, 7], [5, 4, 6], [1, 2, 3]]), [0, 2], "يوجد")
# apl-source:33
تأكد_يساوي(سرج([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [2, 0], "ركن")
# apl-source:34
تأكد_يساوي(سرج([[1, 2], [2, 1]]), [], "لا يوجد")
# apl-source:35
