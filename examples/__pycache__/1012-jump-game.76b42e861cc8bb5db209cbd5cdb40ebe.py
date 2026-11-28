
# apl-source:1
# مثال 1012 — لعبة القفز
# apl-source:2
# Jump game
# apl-source:3
# Demonstrates: أبعد مدى بالجشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1012-jump-game.apl
# apl-source:6

# apl-source:7
# كل خانة تحدد أقصى قفزة منها
# apl-source:8
# نتتبع أبعد خانة يمكن بلوغها ونتوقف لو علقنا
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
def نصل(قفزات):
  # apl-source:19
  ابعد = 0
  # apl-source:20
  for ع in range(len(قفزات)):
    # apl-source:21
    if ع > ابعد:
      # apl-source:22
      return False
    # apl-source:23
    if (ع + قفزات[ع]) > ابعد:
      # apl-source:24
      ابعد = ع + قفزات[ع]
  # apl-source:25
  return True
# apl-source:26

# apl-source:27
تأكد_يساوي(نصل([2, 3, 1, 1, 4]), True, "نصل")
# apl-source:28
تأكد_يساوي(نصل([3, 2, 1, 0, 4]), False, "نعلق عند الصفر")
# apl-source:29
تأكد_يساوي(نصل([0]), True, "خانة واحدة")
# apl-source:30
