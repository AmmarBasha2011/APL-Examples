
# apl-source:1
# مثال 1153 — مجموع اثنين مرتب
# apl-source:2
# Two sum on sorted list
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1153-two-sum-sorted.apl
# apl-source:6

# apl-source:7
# مؤشر من البداية وآخر من النهاية
# apl-source:8
# نحرك حسب مقارنة المجموع بالهدف
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
def زوج(أ, هدف):
  # apl-source:19
  ي = 0
  # apl-source:20
  ن = len(أ) - 1
  # apl-source:21
  while ي < ن:
    # apl-source:22
    مج = أ[ي] + أ[ن]
    # apl-source:23
    if مج == هدف:
      # apl-source:24
      return [ي + 1, ن + 1]
    # apl-source:25
    elif مج < هدف:
      # apl-source:26
      ي = ي + 1
    # apl-source:27
    else:
      # apl-source:28
      ن = ن - 1
  # apl-source:29
  return []
# apl-source:30

# apl-source:31
تأكد_يساوي(زوج([2,7,11,15], 9), [1, 2], "أول")
# apl-source:32
تأكد_يساوي(زوج([2,3,4], 6), [1, 3], "ثان")
# apl-source:33
تأكد_يساوي(زوج([-1,0], -1), [1, 2], "سالب")
# apl-source:34
تأكد_يساوي(زوج([1,2,3], 100), [], "لا حل")
# apl-source:35
