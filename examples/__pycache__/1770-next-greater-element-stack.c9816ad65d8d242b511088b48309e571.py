
# apl-source:1
# مثال 1770 — العنصر الأكبر التالي
# apl-source:2
# Next greater element with stack
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1770-next-greater-element-stack.apl
# apl-source:6

# apl-source:7
# نمر من اليمين مع مكدس
# apl-source:8
# نزيل الأصغر من المكدس
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
def التالي_الأكبر(ق):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in ق:
    # apl-source:21
    ناتج.append(-1)
  # apl-source:22
  مكدس = []
  # apl-source:23
  for ك in range(len(ق) - 1, -1, -1):
    # apl-source:24
    while len(مكدس) > 0 and مكدس[len(مكدس) - 1] <= ق[ك]:
      # apl-source:25
      مكدس.pop()
    # apl-source:26
    if len(مكدس) > 0:
      # apl-source:27
      ناتج[ك] = مكدس[len(مكدس) - 1]
    # apl-source:28
    مكدس.append(ق[ك])
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(التالي_الأكبر([4, 5, 2, 25]), [5, 25, 25, -1], "أربعة")
# apl-source:32
تأكد_يساوي(التالي_الأكبر([3, 2, 1]), [-1, -1, -1], "هابطة")
# apl-source:33
تأكد_يساوي(التالي_الأكبر([1, 2, 3]), [2, 3, -1], "صاعدة")
# apl-source:34
