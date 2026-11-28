
# apl-source:1
# مثال 1354 — أشجار أقل ارتفاعاً
# apl-source:2
# Minimum height trees roots
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1354-min-height-trees.apl
# apl-source:6

# apl-source:7
# نقشر الأوراق طبقة بعد طبقة
# apl-source:8
# ما يبقى في النهاية هو المركز
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
def جذور_دنيا(ن, حواف):
  # apl-source:19
  if ن == 1:
    # apl-source:20
    return [0]
  # apl-source:21
  جيران = []
  # apl-source:22
  for ع in range(ن):
    # apl-source:23
    جيران = جيران + [[]]
  # apl-source:24
  for ح in حواف:
    # apl-source:25
    جيران[ح[0]] = جيران[ح[0]] + [ح[1]]
    # apl-source:26
    جيران[ح[1]] = جيران[ح[1]] + [ح[0]]
  # apl-source:27
  اوراق = []
  # apl-source:28
  for ع in range(ن):
    # apl-source:29
    if len(جيران[ع]) == 1:
      # apl-source:30
      اوراق = اوراق + [ع]
  # apl-source:31
  متبقي = ن
  # apl-source:32
  while متبقي > 2:
    # apl-source:33
    متبقي = متبقي - len(اوراق)
    # apl-source:34
    جديدة = []
    # apl-source:35
    for ور in اوراق:
      # apl-source:36
      ج = جيران[ور][0]
      # apl-source:37
      جيران[ج].remove(ور)
      # apl-source:38
      if len(جيران[ج]) == 1:
        # apl-source:39
        جديدة = جديدة + [ج]
    # apl-source:40
    اوراق = جديدة
  # apl-source:41
  return sorted(اوراق)
# apl-source:42

# apl-source:43
تأكد_يساوي(جذور_دنيا(4, [[1,0],[1,2],[1,3]]), [1], "جذر واحد")
# apl-source:44
تأكد_يساوي(جذور_دنيا(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]), [3,4], "جذران")
# apl-source:45
تأكد_يساوي(جذور_دنيا(1, []), [0], "عقدة")
# apl-source:46
