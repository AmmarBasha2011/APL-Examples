
# apl-source:1
# مثال 1197 — مناطق محاصرة
# apl-source:2
# Surrounded regions
# apl-source:3
# Demonstrates: بحث بالعمق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1197-surrounded-regions.apl
# apl-source:6

# apl-source:7
# نحدد الخانات المتصلة بالحافة ونحميها
# apl-source:8
# وكل ما بقي من O يصبح X
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
def احصر(ش):
  # apl-source:19
  ر_ = len(ش)
  # apl-source:20
  ك_ = len(ش[0])
  # apl-source:21
  مكدس = []
  # apl-source:22
  for ص in range(ر_):
    # apl-source:23
    for ج in range(ك_):
      # apl-source:24
      حافة = (ص == 0) or (ص == ر_ - 1) or (ج == 0) or (ج == ك_ - 1)
      # apl-source:25
      if حافة and (ش[ص][ج] == "O"):
        # apl-source:26
        مكدس = مكدس + [[ص, ج]]
  # apl-source:27
  اتجاهات = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  # apl-source:28
  while len(مكدس) > 0:
    # apl-source:29
    ن = مكدس.pop()
    # apl-source:30
    if ش[ن[0]][ن[1]] == "O":
      # apl-source:31
      ش[ن[0]][ن[1]] = "S"
      # apl-source:32
      for د in اتجاهات:
        # apl-source:33
        ر = ن[0] + د[0]
        # apl-source:34
        ك = ن[1] + د[1]
        # apl-source:35
        if (ر >= 0) and (ر < ر_) and (ك >= 0) and (ك < ك_):
          # apl-source:36
          if ش[ر][ك] == "O":
            # apl-source:37
            مكدس = مكدس + [[ر, ك]]
  # apl-source:38
  for ص in range(ر_):
    # apl-source:39
    for ج in range(ك_):
      # apl-source:40
      if ش[ص][ج] == "O":
        # apl-source:41
        ش[ص][ج] = "X"
      # apl-source:42
      elif ش[ص][ج] == "S":
        # apl-source:43
        ش[ص][ج] = "O"
  # apl-source:44
  return ش
# apl-source:45

# apl-source:46
م = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# apl-source:47
تأكد_يساوي(احصر(م), [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]], "مثال أول")
# apl-source:48
تأكد_يساوي(احصر([["O"]]), [["O"]], "حافة")
# apl-source:49
