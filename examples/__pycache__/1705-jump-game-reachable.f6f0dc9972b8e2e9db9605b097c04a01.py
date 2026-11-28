
# apl-source:1
# مثال 1705 — هل نصل آخر المصفوفة بالقفزات
# apl-source:2
# Jump game reachability
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1705-jump-game-reachable.apl
# apl-source:6

# apl-source:7
# نتتبع أبعد مؤشر
# apl-source:8
# نفشل إن تجاوزنا الوصول
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
def نصل(ق):
  # apl-source:19
  أبعد = 0
  # apl-source:20
  for ك in range(len(ق)):
    # apl-source:21
    if ك > أبعد:
      # apl-source:22
      return False
    # apl-source:23
    أبعد = max(أبعد, ك + ق[ك])
  # apl-source:24
  return True
# apl-source:25

# apl-source:26
تأكد_يساوي(نصل([2, 3, 1, 1, 4]), True, "نصل")
# apl-source:27
تأكد_يساوي(نصل([3, 2, 1, 0, 4]), False, "عالق")
# apl-source:28
تأكد_يساوي(نصل([0]), True, "واحد")
# apl-source:29
