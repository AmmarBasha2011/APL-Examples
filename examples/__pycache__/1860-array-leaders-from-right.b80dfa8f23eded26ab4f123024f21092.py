
# apl-source:1
# مثال 1860 — قادة المصفوفة من اليمين
# apl-source:2
# Array leaders from right
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1860-array-leaders-from-right.apl
# apl-source:6

# apl-source:7
# نمر من اليمين
# apl-source:8
# نحتفظ بأكبر ما رأينا
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
def قادة(ق):
  # apl-source:19
  ناتج = []
  # apl-source:20
  أعلى = -1000000
  # apl-source:21
  for ك in range(len(ق) - 1, -1, -1):
    # apl-source:22
    if ق[ك] > أعلى:
      # apl-source:23
      ناتج.append(ق[ك])
      # apl-source:24
      أعلى = ق[ك]
  # apl-source:25
  ناتج.reverse()
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(قادة([16, 17, 4, 3, 5, 2]), [17, 5, 2], "كلاسيكي")
# apl-source:29
تأكد_يساوي(قادة([1, 2, 3]), [3], "صاعدة")
# apl-source:30
تأكد_يساوي(قادة([3, 2, 1]), [3, 2, 1], "هابطة")
# apl-source:31
