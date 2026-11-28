
# apl-source:1
# مثال 1301 — حلقة في قائمة
# apl-source:2
# Linked list cycle using next array
# apl-source:3
# Demonstrates: فلويد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1301-linked-list-cycle-array.apl
# apl-source:6

# apl-source:7
# كل عقدة لها فهرس التالي
# apl-source:8
# مؤشر سريع وبطيء يلتقيان لو وجدت حلقة
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
def فيها_حلقة(تالي, بداية):
  # apl-source:19
  بطيء = بداية
  # apl-source:20
  سريع = بداية
  # apl-source:21
  while (سريع != -1) and (تالي[سريع] != -1):
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
تأكد_يساوي(فيها_حلقة([1, 2, 3, 1], 0), True, "حلقة")
# apl-source:29
تأكد_يساوي(فيها_حلقة([1, 2, 3, -1], 0), False, "بلا حلقة")
# apl-source:30
تأكد_يساوي(فيها_حلقة([0], 0), True, "حلقة ذاتية")
# apl-source:31
تأكد_يساوي(فيها_حلقة([-1], 0), False, "عقدة وحيدة")
# apl-source:32
