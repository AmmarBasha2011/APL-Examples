
# apl-source:1
# مثال 1682 — أكبر قيمة في كل نافذة
# apl-source:2
# Maximum of each sliding window
# apl-source:3
# Demonstrates: نوافذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1682-sliding-window-max-simple.apl
# apl-source:6

# apl-source:7
# نمرر النافذة على القائمة
# apl-source:8
# نحسب الأكبر في كل موضع
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
def أكبر_النوافذ(ق, ك):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ي in range(len(ق) - ك + 1):
    # apl-source:21
    م = ق[ي]
    # apl-source:22
    for ج in range(ي, ي + ك):
      # apl-source:23
      م = max(م, ق[ج])
    # apl-source:24
    ناتج.append(م)
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(أكبر_النوافذ([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7], "ثلاثة")
# apl-source:28
تأكد_يساوي(أكبر_النوافذ([4, 2], 1), [4, 2], "واحد")
# apl-source:29
