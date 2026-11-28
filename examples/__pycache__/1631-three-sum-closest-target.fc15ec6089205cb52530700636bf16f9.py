
# apl-source:1
# مثال 1631 — أقرب مجموع ثلاثي للهدف
# apl-source:2
# Three sum closest to target
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1631-three-sum-closest-target.apl
# apl-source:6

# apl-source:7
# نرتب ونثبت عنصراً ونحرك مؤشرين
# apl-source:8
# نحتفظ بالأقرب للهدف
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
def أقرب_مجموع(أ, هدف):
  # apl-source:19
  ق = []
  # apl-source:20
  for ع in أ:
    # apl-source:21
    ق.append(ع)
  # apl-source:22
  ق.sort()
  # apl-source:23
  أفضل = ق[0] + ق[1] + ق[2]
  # apl-source:24
  for ع in range(len(ق) - 2):
    # apl-source:25
    ي = ع + 1
    # apl-source:26
    ج = len(ق) - 1
    # apl-source:27
    while ي < ج:
      # apl-source:28
      م = ق[ع] + ق[ي] + ق[ج]
      # apl-source:29
      فرق_جديد = م - هدف
      # apl-source:30
      فرق_أفضل = أفضل - هدف
      # apl-source:31
      if فرق_جديد < 0:
        # apl-source:32
        فرق_جديد = -فرق_جديد
      # apl-source:33
      if فرق_أفضل < 0:
        # apl-source:34
        فرق_أفضل = -فرق_أفضل
      # apl-source:35
      if فرق_جديد < فرق_أفضل:
        # apl-source:36
        أفضل = م
      # apl-source:37
      if م < هدف:
        # apl-source:38
        ي = ي + 1
      # apl-source:39
      elif م > هدف:
        # apl-source:40
        ج = ج - 1
      # apl-source:41
      else:
        # apl-source:42
        return م
  # apl-source:43
  return أفضل
# apl-source:44

# apl-source:45
تأكد_يساوي(أقرب_مجموع([-1, 2, 1, -4], 1), 2, "كلاسيكي")
# apl-source:46
تأكد_يساوي(أقرب_مجموع([0, 0, 0], 1), 0, "أصفار")
# apl-source:47
تأكد_يساوي(أقرب_مجموع([1, 1, 1, 0], 100), 3, "هدف بعيد")
# apl-source:48
