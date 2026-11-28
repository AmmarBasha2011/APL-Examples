
# apl-source:1
# مثال 1755 — توليد الأقواس المتوازنة
# apl-source:2
# Generate balanced parentheses
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1755-generate-parentheses-all.apl
# apl-source:6

# apl-source:7
# لا نغلق أكثر مما فتحنا
# apl-source:8
# نتوقف عند الطول الكامل
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
def ولّد(ن):
  # apl-source:19
  ناتج = []
  # apl-source:20
  دالة_تراجع = 0
  # apl-source:21
  مكدس = [["", 0, 0]]
  # apl-source:22
  while len(مكدس) > 0:
    # apl-source:23
    ح = مكدس.pop()
    # apl-source:24
    if len(ح[0]) == 2 * ن:
      # apl-source:25
      ناتج.append(ح[0])
    # apl-source:26
    else:
      # apl-source:27
      if ح[2] < ح[1]:
        # apl-source:28
        مكدس.append([ح[0] + ")", ح[1], ح[2] + 1])
      # apl-source:29
      if ح[1] < ن:
        # apl-source:30
        مكدس.append([ح[0] + "(", ح[1] + 1, ح[2]])
  # apl-source:31
  ناتج.sort()
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
تأكد_يساوي(ولّد(1), ["()"], "واحد")
# apl-source:35
تأكد_يساوي(ولّد(2), ["(())", "()()"], "اثنان")
# apl-source:36
تأكد_يساوي(len(ولّد(4)), 14, "أربعة")
# apl-source:37
