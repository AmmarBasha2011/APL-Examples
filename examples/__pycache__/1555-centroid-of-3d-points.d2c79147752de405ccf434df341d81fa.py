
# apl-source:1
# مثال 1555 — مركز مجموعة نقاط في الفراغ
# apl-source:2
# Centroid of 3D points
# apl-source:3
# Demonstrates: هندسة ثلاثية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1555-centroid-of-3d-points.apl
# apl-source:6

# apl-source:7
# نجمع كل محور على حدة
# apl-source:8
# نقسم على عدد النقاط
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
def مركز_النقاط(نقاط):
  # apl-source:19
  مجموع = [0, 0, 0]
  # apl-source:20
  for ن in نقاط:
    # apl-source:21
    for ع in range(3):
      # apl-source:22
      مجموع[ع] = مجموع[ع] + ن[ع]
  # apl-source:23
  return [مجموع[0] / len(نقاط), مجموع[1] / len(نقاط), مجموع[2] / len(نقاط)]
# apl-source:24

# apl-source:25
تأكد_يساوي(مركز_النقاط([[0, 0, 0], [3, 0, 0], [0, 3, 0], [0, 0, 3]]), [0.75, 0.75, 0.75], "رباعي")
# apl-source:26
تأكد_يساوي(مركز_النقاط([[1, 2, 3]]), [1.0, 2.0, 3.0], "نقطة")
# apl-source:27
