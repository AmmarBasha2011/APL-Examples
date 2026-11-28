
# apl-source:1
# مثال 1549 — المسافة بين نقطتين في الفراغ
# apl-source:2
# Distance between two 3D points
# apl-source:3
# Demonstrates: هندسة ثلاثية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1549-distance-between-3d-points.apl
# apl-source:6

# apl-source:7
# نطرح كل إحداثي
# apl-source:8
# نطبق نظرية فيثاغورس في ثلاثة أبعاد
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
def مسافة_ثلاثية(أ, ب):
  # apl-source:19
  س = أ[0] - ب[0]
  # apl-source:20
  ص = أ[1] - ب[1]
  # apl-source:21
  ع = أ[2] - ب[2]
  # apl-source:22
  return (س * س + ص * ص + ع * ع) ** 0.5
# apl-source:23

# apl-source:24
تأكد_يساوي(مسافة_ثلاثية([0, 0, 0], [1, 2, 2]), 3.0, "ثلاثة")
# apl-source:25
تأكد_يساوي(مسافة_ثلاثية([1, 1, 1], [1, 1, 1]), 0.0, "نفس النقطة")
# apl-source:26
تأكد_يساوي(مسافة_ثلاثية([0, 0, 0], [2, 3, 6]), 7.0, "سبعة")
# apl-source:27
