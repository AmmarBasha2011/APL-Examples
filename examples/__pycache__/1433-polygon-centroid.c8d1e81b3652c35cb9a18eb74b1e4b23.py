
# apl-source:1
# مثال 1433 — مركز ثقل مضلع
# apl-source:2
# Polygon centroid by shoelace
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1433-polygon-centroid.apl
# apl-source:6

# apl-source:7
# نحسب المساحة الموقعة
# apl-source:8
# ثم متوسط الإحداثيات موزوناً بالضرب التقاطعي
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
def مركز_الثقل(نقاط):
  # apl-source:19
  ن = len(نقاط)
  # apl-source:20
  مساحة = 0
  # apl-source:21
  مس = 0
  # apl-source:22
  مص = 0
  # apl-source:23
  for ع in range(ن):
    # apl-source:24
    أ = نقاط[ع]
    # apl-source:25
    ب = نقاط[(ع + 1) % ن]
    # apl-source:26
    ض = أ[0] * ب[1] - ب[0] * أ[1]
    # apl-source:27
    مساحة = مساحة + ض
    # apl-source:28
    مس = مس + (أ[0] + ب[0]) * ض
    # apl-source:29
    مص = مص + (أ[1] + ب[1]) * ض
  # apl-source:30
  مساحة = مساحة / 2
  # apl-source:31
  return [مس / (6 * مساحة), مص / (6 * مساحة)]
# apl-source:32

# apl-source:33
تأكد_يساوي(مركز_الثقل([[0,0],[4,0],[4,4],[0,4]]), [2.0, 2.0], "مربع")
# apl-source:34
تأكد_يساوي(مركز_الثقل([[0,0],[6,0],[0,3]]), [2.0, 1.0], "مثلث")
# apl-source:35
