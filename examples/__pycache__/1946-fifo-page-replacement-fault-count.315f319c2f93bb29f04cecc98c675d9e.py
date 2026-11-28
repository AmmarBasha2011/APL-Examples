
# apl-source:1
# مثال 1946 — استبدال الصفحات بنظام الأول دخولا
# apl-source:2
# FIFO page replacement faults
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1946-fifo-page-replacement-fault-count.apl
# apl-source:6

# apl-source:7
# # الطابور يحفظ ترتيب دخول الصفحات
# apl-source:8
# # كل صفحة غير موجودة تعد خطأ صفحة
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
    if (ص in ذاكرة) == False:
      # apl-source:23
      عدد = عدد + 1
      # apl-source:24
      if len(ذاكرة) == اطارات:
        # apl-source:25
        ذاكرة.pop(0)
      # apl-source:26
      ذاكرة = ذاكرة + [ص]
  # apl-source:27
  return عدد
# apl-source:28

# apl-source:29
س = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
# apl-source:30
تأكد_يساوي(اخطاء(س, 3), 15, "ثلاثة إطارات")
# apl-source:31
تأكد_يساوي(اخطاء(س, 4), 10, "أربعة إطارات")
# apl-source:32
تأكد_يساوي(اخطاء([1, 1, 1], 1), 1, "تكرار")
# apl-source:33
