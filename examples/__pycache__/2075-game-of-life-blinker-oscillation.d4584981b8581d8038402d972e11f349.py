
# apl-source:1
# مثال 2075 — نبضة لعبة الحياة بعد خطوتين
# apl-source:2
# Game of life blinker
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2075-game-of-life-blinker-oscillation.apl
# apl-source:6

# apl-source:7
# # نطبق القواعد على شبكة 5×5
# apl-source:8
# # ونتحقق من الدورية
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
def خطوة(ش):
  # apl-source:19
  ن = len(ش)
  # apl-source:20
  خرج = []
  # apl-source:21
  for ي in range(ن):
    # apl-source:22
    صف = []
    # apl-source:23
    for ك in range(ن):
      # apl-source:24
      جيران = 0
      # apl-source:25
      for د1 in [-1, 0, 1]:
        # apl-source:26
        for د2 in [-1, 0, 1]:
          # apl-source:27
          if (د1 != 0 or د2 != 0) and ي + د1 >= 0 and ي + د1 < ن and ك + د2 >= 0 and ك + د2 < ن:
            # apl-source:28
            جيران = جيران + ش[ي + د1][ك + د2]
      # apl-source:29
      if ش[ي][ك] == 1 and (جيران == 2 or جيران == 3):
        # apl-source:30
        صف = صف + [1]
      # apl-source:31
      elif ش[ي][ك] == 0 and جيران == 3:
        # apl-source:32
        صف = صف + [1]
      # apl-source:33
      else:
        # apl-source:34
        صف = صف + [0]
    # apl-source:35
    خرج = خرج + [صف]
  # apl-source:36
  return خرج
# apl-source:37

# apl-source:38
افقي = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# apl-source:39
راسي = خطوة(افقي)
# apl-source:40
تأكد_يساوي(راسي[1][2], 1, "صاعد")
# apl-source:41
تأكد_يساوي(راسي[2][1], 0, "اختفى يسارا")
# apl-source:42
تأكد_يساوي(خطوة(راسي), افقي, "عودة")
# apl-source:43
