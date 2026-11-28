
# apl-source:1
# مثال 1438 — أكثر نقاط على خط
# apl-source:2
# Max points on a line
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1438-max-points-on-line.apl
# apl-source:6

# apl-source:7
# نجرب كل زوج كخط
# apl-source:8
# ونعد النقاط التي تحقق الجداء التقاطعي صفر
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
def اكثر_نقاط(نقاط):
  # apl-source:19
  ن = len(نقاط)
  # apl-source:20
  if ن <= 2:
    # apl-source:21
    return ن
  # apl-source:22
  افضل = 2
  # apl-source:23
  for ي in range(ن):
    # apl-source:24
    for ك in range(ي + 1, ن):
      # apl-source:25
      عدد = 0
      # apl-source:26
      for ل in range(ن):
        # apl-source:27
        ض = (نقاط[ك][0] - نقاط[ي][0]) * (نقاط[ل][1] - نقاط[ي][1]) - (نقاط[ك][1] - نقاط[ي][1]) * (نقاط[ل][0] - نقاط[ي][0])
        # apl-source:28
        if ض == 0:
          # apl-source:29
          عدد = عدد + 1
      # apl-source:30
      if عدد > افضل:
        # apl-source:31
        افضل = عدد
  # apl-source:32
  return افضل
# apl-source:33

# apl-source:34
تأكد_يساوي(اكثر_نقاط([[1,1],[2,2],[3,3]]), 3, "ثلاث")
# apl-source:35
تأكد_يساوي(اكثر_نقاط([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]), 4, "أربع")
# apl-source:36
تأكد_يساوي(اكثر_نقاط([[0,0]]), 1, "نقطة")
# apl-source:37
