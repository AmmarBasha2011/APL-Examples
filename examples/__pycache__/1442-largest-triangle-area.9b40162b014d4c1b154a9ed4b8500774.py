
# apl-source:1
# مثال 1442 — أكبر مثلث
# apl-source:2
# Largest triangle area from points
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1442-largest-triangle-area.apl
# apl-source:6

# apl-source:7
# نجرب كل ثلاث نقاط
# apl-source:8
# مساحة المثلث نصف القيمة المطلقة للجداء التقاطعي
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
def اكبر_مثلث(ن):
  # apl-source:19
  افضل = 0
  # apl-source:20
  for ي in range(len(ن)):
    # apl-source:21
    for ك in range(ي + 1, len(ن)):
      # apl-source:22
      for ل in range(ك + 1, len(ن)):
        # apl-source:23
        ض = (ن[ك][0] - ن[ي][0]) * (ن[ل][1] - ن[ي][1]) - (ن[ك][1] - ن[ي][1]) * (ن[ل][0] - ن[ي][0])
        # apl-source:24
        if ض < 0:
          # apl-source:25
          ض = -ض
        # apl-source:26
        if ض > افضل:
          # apl-source:27
          افضل = ض
  # apl-source:28
  return افضل / 2
# apl-source:29

# apl-source:30
تأكد_يساوي(اكبر_مثلث([[0,0],[0,1],[1,0],[0,2],[2,0]]), 2.0, "اثنان")
# apl-source:31
تأكد_يساوي(اكبر_مثلث([[1,0],[0,0],[0,1]]), 0.5, "نصف")
# apl-source:32
