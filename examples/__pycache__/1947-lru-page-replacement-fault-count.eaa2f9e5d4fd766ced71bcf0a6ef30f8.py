
# apl-source:1
# مثال 1947 — استبدال الصفحات الأقل استخداما حديثا
# apl-source:2
# LRU page replacement faults
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1947-lru-page-replacement-fault-count.apl
# apl-source:6

# apl-source:7
# # عند كل وصول ننقل الصفحة لآخر القائمة
# apl-source:8
# # أول القائمة هو الأقدم استخداما
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
def اخطاء(صفحات, اطارات):
  # apl-source:19
  ذاكرة = []
  # apl-source:20
  عدد = 0
  # apl-source:21
  for ص in صفحات:
    # apl-source:22
    if ص in ذاكرة:
      # apl-source:23
      ذاكرة.remove(ص)
    # apl-source:24
    else:
      # apl-source:25
      عدد = عدد + 1
      # apl-source:26
      if len(ذاكرة) == اطارات:
        # apl-source:27
        ذاكرة.pop(0)
    # apl-source:28
    ذاكرة = ذاكرة + [ص]
  # apl-source:29
  return عدد
# apl-source:30

# apl-source:31
س = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
# apl-source:32
تأكد_يساوي(اخطاء(س, 3), 12, "ثلاثة إطارات")
# apl-source:33
تأكد_يساوي(اخطاء(س, 4), 8, "أربعة إطارات")
# apl-source:34
تأكد_يساوي(اخطاء([1, 2, 1, 2], 2), 2, "تكرار")
# apl-source:35
