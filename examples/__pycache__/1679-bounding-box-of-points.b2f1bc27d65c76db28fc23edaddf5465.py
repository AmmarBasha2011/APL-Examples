
# apl-source:1
# مثال 1679 — المستطيل المحيط بالنقاط
# apl-source:2
# Bounding box of points
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1679-bounding-box-of-points.apl
# apl-source:6

# apl-source:7
# نمر على النقاط
# apl-source:8
# نحدث الحدود الأربعة
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
def مستطيل_محيط(نقاط):
  # apl-source:19
  س_أصغر = نقاط[0][0]
  # apl-source:20
  س_أكبر = نقاط[0][0]
  # apl-source:21
  ص_أصغر = نقاط[0][1]
  # apl-source:22
  ص_أكبر = نقاط[0][1]
  # apl-source:23
  for ن in نقاط:
    # apl-source:24
    س_أصغر = min(س_أصغر, ن[0])
    # apl-source:25
    س_أكبر = max(س_أكبر, ن[0])
    # apl-source:26
    ص_أصغر = min(ص_أصغر, ن[1])
    # apl-source:27
    ص_أكبر = max(ص_أكبر, ن[1])
  # apl-source:28
  return [س_أصغر, ص_أصغر, س_أكبر, ص_أكبر]
# apl-source:29

# apl-source:30
تأكد_يساوي(مستطيل_محيط([[1, 5], [3, 2], [-1, 4]]), [-1, 2, 3, 5], "ثلاث نقاط")
# apl-source:31
تأكد_يساوي(مستطيل_محيط([[2, 2]]), [2, 2, 2, 2], "نقطة")
# apl-source:32
