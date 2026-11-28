
# apl-source:1
# مثال 1573 — اختيار أكبر عدد أنشطة
# apl-source:2
# Activity selection count
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1573-activity-selection-count.apl
# apl-source:6

# apl-source:7
# نرتب بحسب وقت النهاية
# apl-source:8
# نختار كل نشاط يبدأ بعد انتهاء المختار
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
def اختر_الأنشطة(أنشطة):
  # apl-source:19
  مرتبة = []
  # apl-source:20
  for ن in أنشطة:
    # apl-source:21
    مرتبة.append([ن[1], ن[0]])
  # apl-source:22
  مرتبة.sort()
  # apl-source:23
  آخر = -1
  # apl-source:24
  عد = 0
  # apl-source:25
  for ن in مرتبة:
    # apl-source:26
    if ن[1] >= آخر:
      # apl-source:27
      عد = عد + 1
      # apl-source:28
      آخر = ن[0]
  # apl-source:29
  return عد
# apl-source:30

# apl-source:31
تأكد_يساوي(اختر_الأنشطة([[1, 4], [3, 5], [0, 6], [5, 7], [8, 9], [5, 9]]), 3, "ثلاثة")
# apl-source:32
تأكد_يساوي(اختر_الأنشطة([[1, 2], [2, 3], [3, 4]]), 3, "متصلة")
# apl-source:33
تأكد_يساوي(اختر_الأنشطة([]), 0, "فارغة")
# apl-source:34
