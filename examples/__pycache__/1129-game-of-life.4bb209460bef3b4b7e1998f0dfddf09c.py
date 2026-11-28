
# apl-source:1
# مثال 1129 — لعبة الحياة
# apl-source:2
# Conway's game of life
# apl-source:3
# Demonstrates: جيران ثمانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1129-game-of-life.apl
# apl-source:6

# apl-source:7
# الخلية الحية تبقى بجارين أو ثلاثة
# apl-source:8
# والميتة تحيا بثلاثة جيران بالضبط
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
def جيران(ل, ص, ج):
  # apl-source:19
  ع = 0
  # apl-source:20
  for د1 in [-1, 0, 1]:
    # apl-source:21
    for د2 in [-1, 0, 1]:
      # apl-source:22
      if (د1 != 0) or (د2 != 0):
        # apl-source:23
        ر = ص + د1
        # apl-source:24
        ك = ج + د2
        # apl-source:25
        if (ر >= 0) and (ر < len(ل)):
          # apl-source:26
          if (ك >= 0) and (ك < len(ل[0])):
            # apl-source:27
            ع = ع + ل[ر][ك]
  # apl-source:28
  return ع
# apl-source:29

# apl-source:30
def خطوة(ل):
  # apl-source:31
  ناتج = []
  # apl-source:32
  for ص in range(len(ل)):
    # apl-source:33
    صف = []
    # apl-source:34
    for ج in range(len(ل[0])):
      # apl-source:35
      ع = جيران(ل, ص, ج)
      # apl-source:36
      حية = 0
      # apl-source:37
      if ل[ص][ج] == 1:
        # apl-source:38
        if (ع == 2) or (ع == 3):
          # apl-source:39
          حية = 1
      # apl-source:40
      else:
        # apl-source:41
        if ع == 3:
          # apl-source:42
          حية = 1
      # apl-source:43
      صف = صف + [حية]
    # apl-source:44
    ناتج = ناتج + [صف]
  # apl-source:45
  return ناتج
# apl-source:46

# apl-source:47
وميض = [[0,0,0],[1,1,1],[0,0,0]]
# apl-source:48
تأكد_يساوي(خطوة(وميض), [[0,1,0],[0,1,0],[0,1,0]], "وميض")
# apl-source:49
تأكد_يساوي(خطوة(خطوة(وميض)), وميض, "دورة")
# apl-source:50
مربع = [[1,1],[1,1]]
# apl-source:51
تأكد_يساوي(خطوة(مربع), مربع, "مستقر")
# apl-source:52
تأكد_يساوي(خطوة([[0,0],[0,0]]), [[0,0],[0,0]], "ميتة")
# apl-source:53
