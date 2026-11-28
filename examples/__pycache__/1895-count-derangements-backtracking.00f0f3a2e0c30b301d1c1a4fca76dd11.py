
# apl-source:1
# مثال 1895 — عدد التبديلات بلا نقطة ثابتة
# apl-source:2
# Count derangements by backtracking
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1895-count-derangements-backtracking.apl
# apl-source:6

# apl-source:7
# نملأ المواضع واحدا واحدا
# apl-source:8
# نمنع العنصر من موضعه الأصلي
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
def اختلال(ن, موضع, مستعمل):
  # apl-source:19
  if موضع == ن:
    # apl-source:20
    return 1
  # apl-source:21
  عد = 0
  # apl-source:22
  for ق in range(ن):
    # apl-source:23
    if ق != موضع and (ق in مستعمل) == False:
      # apl-source:24
      عد = عد + اختلال(ن, موضع + 1, مستعمل + [ق])
  # apl-source:25
  return عد
# apl-source:26

# apl-source:27
تأكد_يساوي(اختلال(3, 0, []), 2, "ثلاثة")
# apl-source:28
تأكد_يساوي(اختلال(4, 0, []), 9, "أربعة")
# apl-source:29
تأكد_يساوي(اختلال(1, 0, []), 0, "واحد")
# apl-source:30
