
# apl-source:1
# مثال 1081 — الأعداد القابلة للقسمة على خاناتها
# apl-source:2
# Self dividing numbers
# apl-source:3
# Demonstrates: فحص الخانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1081-self-dividing.apl
# apl-source:6

# apl-source:7
# العدد المحتوي على صفر مرفوض
# apl-source:8
# وكل خانة يجب أن تقسمه بلا باقي
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
def ذاتي(ن):
  # apl-source:19
  م = ن
  # apl-source:20
  while م > 0:
    # apl-source:21
    خ = م % 10
    # apl-source:22
    if (خ == 0) or ((ن % خ) != 0):
      # apl-source:23
      return False
    # apl-source:24
    م = م // 10
  # apl-source:25
  return True
# apl-source:26

# apl-source:27
def كل_الذاتية(بداية, نهاية):
  # apl-source:28
  ناتج = []
  # apl-source:29
  for ن in range(بداية, نهاية + 1):
    # apl-source:30
    if ذاتي(ن):
      # apl-source:31
      ناتج = ناتج + [ن]
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
تأكد_يساوي(كل_الذاتية(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22], "حتى 22")
# apl-source:35
تأكد_يساوي(كل_الذاتية(47, 85), [48, 55, 66, 77], "من 47 إلى 85")
# apl-source:36
تأكد_يساوي(ذاتي(10), False, "فيه صفر")
# apl-source:37
