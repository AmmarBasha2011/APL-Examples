
# apl-source:1
# مثال 1578 — ترتيب مكدس بمكدس مساعد
# apl-source:2
# Sort a stack using another stack
# apl-source:3
# Demonstrates: مكدسات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1578-sort-stack-with-temp.apl
# apl-source:6

# apl-source:7
# نسحب من الأصلي
# apl-source:8
# نرجع للأصلي كل ما هو أكبر في المساعد
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
def رتب_المكدس(مكدس):
  # apl-source:19
  مساعد = []
  # apl-source:20
  while len(مكدس) > 0:
    # apl-source:21
    ق = مكدس.pop()
    # apl-source:22
    while len(مساعد) > 0 and مساعد[len(مساعد) - 1] > ق:
      # apl-source:23
      مكدس.append(مساعد.pop())
    # apl-source:24
    مساعد.append(ق)
  # apl-source:25
  return مساعد
# apl-source:26

# apl-source:27
تأكد_يساوي(رتب_المكدس([34, 3, 31, 98, 92, 23]), [3, 23, 31, 34, 92, 98], "ستة")
# apl-source:28
تأكد_يساوي(رتب_المكدس([]), [], "فارغ")
# apl-source:29
تأكد_يساوي(رتب_المكدس([2, 1]), [1, 2], "اثنان")
# apl-source:30
