
# apl-source:1
# مثال 1374 — لعبة الحجارة الثانية
# apl-source:2
# Stone game II
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1374-stone-game-two.apl
# apl-source:6

# apl-source:7
# م يتغير بحسب آخر أخذ
# apl-source:8
# نستخدم مجاميع اللواحق وجدول الحالات
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
def اقصى_حجارة(أكوام):
  # apl-source:19
  ن = len(أكوام)
  # apl-source:20
  لاحقة = [0] * (ن + 1)
  # apl-source:21
  for ع in range(ن - 1, -1, -1):
    # apl-source:22
    لاحقة[ع] = لاحقة[ع + 1] + أكوام[ع]
  # apl-source:23
  د = []
  # apl-source:24
  for ع in range(ن + 1):
    # apl-source:25
    د = د + [[0] * (ن + 1)]
  # apl-source:26
  for ع in range(ن - 1, -1, -1):
    # apl-source:27
    for م in range(1, ن + 1):
      # apl-source:28
      if ع + 2 * م >= ن:
        # apl-source:29
        د[ع][م] = لاحقة[ع]
      # apl-source:30
      else:
        # apl-source:31
        افضل = 0
        # apl-source:32
        for س in range(1, 2 * م + 1):
          # apl-source:33
          قيمة = لاحقة[ع] - د[ع + س][max(م, س)]
          # apl-source:34
          if قيمة > افضل:
            # apl-source:35
            افضل = قيمة
        # apl-source:36
        د[ع][م] = افضل
  # apl-source:37
  return د[0][1]
# apl-source:38

# apl-source:39
تأكد_يساوي(اقصى_حجارة([2,7,9,4,4]), 10, "عشرة")
# apl-source:40
تأكد_يساوي(اقصى_حجارة([1,2,3,4,5,100]), 104, "مئة وأربعة")
# apl-source:41
تأكد_يساوي(اقصى_حجارة([5]), 5, "كومة واحدة")
# apl-source:42
