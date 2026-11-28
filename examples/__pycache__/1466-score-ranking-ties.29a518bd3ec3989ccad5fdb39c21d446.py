
# apl-source:1
# مثال 1466 — ترتيب النتائج مع التعادل
# apl-source:2
# Ranking scores with ties
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1466-score-ranking-ties.apl
# apl-source:6

# apl-source:7
# نرتب النتائج تنازلياً
# apl-source:8
# المركز التالي يقفز بعدد المتعادلين
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
def المراكز(نتائج):
  # apl-source:19
  مرتبة = []
  # apl-source:20
  for ن in نتائج:
    # apl-source:21
    مرتبة.append(ن)
  # apl-source:22
  مرتبة.sort()
  # apl-source:23
  مرتبة.reverse()
  # apl-source:24
  مركز = {}
  # apl-source:25
  for ع in range(len(مرتبة)):
    # apl-source:26
    موجود = مرتبة[ع] in مركز
    # apl-source:27
    if موجود == False:
      # apl-source:28
      مركز[مرتبة[ع]] = ع + 1
  # apl-source:29
  ناتج = []
  # apl-source:30
  for ن in نتائج:
    # apl-source:31
    ناتج.append(مركز[ن])
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
تأكد_يساوي(المراكز([100, 90, 90, 80]), [1, 2, 2, 4], "تعادل")
# apl-source:35
تأكد_يساوي(المراكز([5, 5, 5]), [1, 1, 1], "الكل متعادل")
# apl-source:36
تأكد_يساوي(المراكز([1, 2, 3]), [3, 2, 1], "بلا تعادل")
# apl-source:37
