
# apl-source:1
# مثال 1765 — كشف الدورة في قائمة مترابطة
# apl-source:2
# Cycle detection in linked list
# apl-source:3
# Demonstrates: قوائم مترابطة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1765-linked-list-cycle-detect-floyd.apl
# apl-source:6

# apl-source:7
# إن التقيا فهناك دورة
# apl-source:8
# النهاية سالب واحد
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
def فيها_دورة(تالي, رأس):
  # apl-source:19
  بطيء = رأس
  # apl-source:20
  سريع = رأس
  # apl-source:21
  while سريع != -1 and تالي[سريع] != -1:
    # apl-source:22
    بطيء = تالي[بطيء]
    # apl-source:23
    سريع = تالي[تالي[سريع]]
    # apl-source:24
    if بطيء == سريع:
      # apl-source:25
      return True
  # apl-source:26
  return False
# apl-source:27

# apl-source:28
تأكد_يساوي(فيها_دورة([1, 2, 3, -1], 0), False, "بلا دورة")
# apl-source:29
تأكد_يساوي(فيها_دورة([1, 2, 3, 1], 0), True, "دورة")
# apl-source:30
تأكد_يساوي(فيها_دورة([0], 0), True, "ذاتية")
# apl-source:31
