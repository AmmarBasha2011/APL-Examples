
# apl-source:1
# مثال 1449 — الصندوق المحيط
# apl-source:2
# Bounding box of points
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1449-bounding-box-points.apl
# apl-source:6

# apl-source:7
# نتتبع أصغر وأكبر قيمة لكل إحداثي
# apl-source:8
# نعيد الزاويتين
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
def صندوق(نقاط):
  # apl-source:19
  س0 = نقاط[0][0]
  # apl-source:20
  ص0 = نقاط[0][1]
  # apl-source:21
  س1 = س0
  # apl-source:22
  ص1 = ص0
  # apl-source:23
  for ن in نقاط:
    # apl-source:24
    س0 = min(س0, ن[0])
    # apl-source:25
    ص0 = min(ص0, ن[1])
    # apl-source:26
    س1 = max(س1, ن[0])
    # apl-source:27
    ص1 = max(ص1, ن[1])
  # apl-source:28
  return [س0, ص0, س1, ص1]
# apl-source:29

# apl-source:30
تأكد_يساوي(صندوق([[1,2],[3,-1],[0,5]]), [0, -1, 3, 5], "ثلاث نقاط")
# apl-source:31
تأكد_يساوي(صندوق([[2,2]]), [2, 2, 2, 2], "نقطة")
# apl-source:32
تأكد_يساوي(صندوق([[-1,-1],[1,1]]), [-1, -1, 1, 1], "قطر")
# apl-source:33
