
# apl-source:1
# مثال 1051 — تصفير المصفوفة
# apl-source:2
# Set matrix zeroes
# apl-source:3
# Demonstrates: تسجيل الصفوف والأعمدة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1051-set-matrix-zeroes.apl
# apl-source:6

# apl-source:7
# نسجل أولاً الصفوف والأعمدة التي تحوي صفراً
# apl-source:8
# ثم نصفرها كلها بعد المسح حتى لا يتسلسل الأثر
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
def صفّر(م):
  # apl-source:19
  صفوف = []
  # apl-source:20
  اعمدة = []
  # apl-source:21
  for ر in range(len(م)):
    # apl-source:22
    for ك in range(len(م[0])):
      # apl-source:23
      if م[ر][ك] == 0:
        # apl-source:24
        صفوف = صفوف + [ر]
        # apl-source:25
        اعمدة = اعمدة + [ك]
  # apl-source:26
  for ر in range(len(م)):
    # apl-source:27
    for ك in range(len(م[0])):
      # apl-source:28
      if (ر in صفوف) or (ك in اعمدة):
        # apl-source:29
        م[ر][ك] = 0
  # apl-source:30
  return م
# apl-source:31

# apl-source:32
تأكد_يساوي(صفّر([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), [[1, 0, 1], [0, 0, 0], [1, 0, 1]], "صفر في الوسط")
# apl-source:33
تأكد_يساوي(صفّر([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]), [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], "صفران")
# apl-source:34
تأكد_يساوي(صفّر([[1, 2], [3, 4]]), [[1, 2], [3, 4]], "بلا أصفار")
# apl-source:35
