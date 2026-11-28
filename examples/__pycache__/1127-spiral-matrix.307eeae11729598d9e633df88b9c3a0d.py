
# apl-source:1
# مثال 1127 — مصفوفة حلزونية
# apl-source:2
# Spiral matrix order
# apl-source:3
# Demonstrates: حدود أربعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1127-spiral-matrix.apl
# apl-source:6

# apl-source:7
# نضيق الحدود الأربعة بعد كل ضلع
# apl-source:8
# نقرأ العلوي ثم الأيمن ثم السفلي ثم الأيسر
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
def حلزون(م):
  # apl-source:19
  ناتج = []
  # apl-source:20
  if len(م) == 0:
    # apl-source:21
    return ناتج
  # apl-source:22
  أعلى = 0
  # apl-source:23
  أسفل = len(م) - 1
  # apl-source:24
  يسار = 0
  # apl-source:25
  يمين = len(م[0]) - 1
  # apl-source:26
  while (أعلى <= أسفل) and (يسار <= يمين):
    # apl-source:27
    for ج in range(يسار, يمين + 1):
      # apl-source:28
      ناتج = ناتج + [م[أعلى][ج]]
    # apl-source:29
    أعلى = أعلى + 1
    # apl-source:30
    for ص in range(أعلى, أسفل + 1):
      # apl-source:31
      ناتج = ناتج + [م[ص][يمين]]
    # apl-source:32
    يمين = يمين - 1
    # apl-source:33
    if أعلى <= أسفل:
      # apl-source:34
      for ج in range(يمين, يسار - 1, -1):
        # apl-source:35
        ناتج = ناتج + [م[أسفل][ج]]
      # apl-source:36
      أسفل = أسفل - 1
    # apl-source:37
    if يسار <= يمين:
      # apl-source:38
      for ص in range(أسفل, أعلى - 1, -1):
        # apl-source:39
        ناتج = ناتج + [م[ص][يسار]]
      # apl-source:40
      يسار = يسار + 1
  # apl-source:41
  return ناتج
# apl-source:42

# apl-source:43
تأكد_يساوي(حلزون([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5], "ثلاثة في ثلاثة")
# apl-source:44
تأكد_يساوي(حلزون([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7], "ثلاثة في أربعة")
# apl-source:45
تأكد_يساوي(حلزون([[1],[2],[3]]), [1,2,3], "عمود")
# apl-source:46
تأكد_يساوي(حلزون([]), [], "فارغة")
# apl-source:47
