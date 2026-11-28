
# apl-source:1
# مثال 2000 — مجموع عددين في قائمة مرتبة
# apl-source:2
# Two sum in sorted list
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2000-two-sum-sorted-two-pointers.apl
# apl-source:6

# apl-source:7
# # إن كان المجموع صغيرا نحرك المؤشر الأيسر
# apl-source:8
# # وإن كان كبيرا نحرك الأيمن
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
def مجموع_اثنين(ق, هدف):
  # apl-source:19
  ي = 0
  # apl-source:20
  ل = len(ق) - 1
  # apl-source:21
  while ي < ل:
    # apl-source:22
    م = ق[ي] + ق[ل]
    # apl-source:23
    if م == هدف:
      # apl-source:24
      return [ي, ل]
    # apl-source:25
    elif م < هدف:
      # apl-source:26
      ي = ي + 1
    # apl-source:27
    else:
      # apl-source:28
      ل = ل - 1
  # apl-source:29
  return []
# apl-source:30

# apl-source:31
تأكد_يساوي(مجموع_اثنين([2, 7, 11, 15], 9), [0, 1], "أول زوج")
# apl-source:32
تأكد_يساوي(مجموع_اثنين([2, 3, 4], 6), [0, 2], "طرفان")
# apl-source:33
تأكد_يساوي(مجموع_اثنين([1, 2], 10), [], "لا يوجد")
# apl-source:34
