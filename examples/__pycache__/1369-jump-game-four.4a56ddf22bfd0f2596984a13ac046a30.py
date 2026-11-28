
# apl-source:1
# مثال 1369 — قفزات أربعة
# apl-source:2
# Jump game IV equal values
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1369-jump-game-four.apl
# apl-source:6

# apl-source:7
# من i نقفز إلى i±1 أو لأي موضع بنفس القيمة
# apl-source:8
# نفرغ قائمة القيمة بعد استخدامها
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
def اقل_قفزات(مصفوفة):
  # apl-source:19
  ن = len(مصفوفة)
  # apl-source:20
  if ن == 1:
    # apl-source:21
    return 0
  # apl-source:22
  مواضع = {}
  # apl-source:23
  for ع in range(ن):
    # apl-source:24
    if مصفوفة[ع] not in مواضع:
      # apl-source:25
      مواضع[مصفوفة[ع]] = []
    # apl-source:26
    مواضع[مصفوفة[ع]] = مواضع[مصفوفة[ع]] + [ع]
  # apl-source:27
  بعد_ = [-1] * ن
  # apl-source:28
  بعد_[0] = 0
  # apl-source:29
  طابور = [0]
  # apl-source:30
  ك = 0
  # apl-source:31
  while ك < len(طابور):
    # apl-source:32
    ق = طابور[ك]
    # apl-source:33
    ك = ك + 1
    # apl-source:34
    جيران = [ق - 1, ق + 1]
    # apl-source:35
    for م in مواضع[مصفوفة[ق]]:
      # apl-source:36
      جيران = جيران + [م]
    # apl-source:37
    مواضع[مصفوفة[ق]] = []
    # apl-source:38
    for ج in جيران:
      # apl-source:39
      if (ج >= 0) and (ج < ن):
        # apl-source:40
        if بعد_[ج] == -1:
          # apl-source:41
          بعد_[ج] = بعد_[ق] + 1
          # apl-source:42
          if ج == ن - 1:
            # apl-source:43
            return بعد_[ج]
          # apl-source:44
          طابور = طابور + [ج]
  # apl-source:45
  return بعد_[ن - 1]
# apl-source:46

# apl-source:47
تأكد_يساوي(اقل_قفزات([100,-23,-23,404,100,23,23,23,3,404]), 3, "ثلاث قفزات")
# apl-source:48
تأكد_يساوي(اقل_قفزات([7]), 0, "عنصر")
# apl-source:49
تأكد_يساوي(اقل_قفزات([7,6,9,6,9,6,9,7]), 1, "قفزة واحدة")
# apl-source:50
