
# apl-source:1
# مثال 1326 — جزر مختلفة
# apl-source:2
# Number of distinct islands
# apl-source:3
# Demonstrates: بحث بالعمق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1326-number-of-distinct-islands.apl
# apl-source:6

# apl-source:7
# نسجل إحداثيات كل جزيرة نسبة لأول خلية
# apl-source:8
# ونعد الأشكال المختلفة
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
def اشكال(ش):
  # apl-source:19
  ر_ = len(ش)
  # apl-source:20
  ك_ = len(ش[0])
  # apl-source:21
  مرئي = []
  # apl-source:22
  for ع in range(ر_):
    # apl-source:23
    مرئي = مرئي + [[False] * ك_]
  # apl-source:24
  كل = []
  # apl-source:25
  اتجاهات = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  # apl-source:26
  for ص in range(ر_):
    # apl-source:27
    for ج in range(ك_):
      # apl-source:28
      if (ش[ص][ج] == 1) and (not مرئي[ص][ج]):
        # apl-source:29
        مكدس = [[ص, ج]]
        # apl-source:30
        مرئي[ص][ج] = True
        # apl-source:31
        شكل = []
        # apl-source:32
        while len(مكدس) > 0:
          # apl-source:33
          ن = مكدس.pop()
          # apl-source:34
          شكل = شكل + [[ن[0] - ص, ن[1] - ج]]
          # apl-source:35
          for د in اتجاهات:
            # apl-source:36
            ر = ن[0] + د[0]
            # apl-source:37
            ك = ن[1] + د[1]
            # apl-source:38
            if (ر >= 0) and (ر < ر_) and (ك >= 0) and (ك < ك_):
              # apl-source:39
              if (ش[ر][ك] == 1) and (not مرئي[ر][ك]):
                # apl-source:40
                مرئي[ر][ك] = True
                # apl-source:41
                مكدس = مكدس + [[ر, ك]]
        # apl-source:42
        شكل = sorted(شكل)
        # apl-source:43
        if شكل not in كل:
          # apl-source:44
          كل = كل + [شكل]
  # apl-source:45
  return len(كل)
# apl-source:46

# apl-source:47
تأكد_يساوي(اشكال([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]), 1, "شكل واحد")
# apl-source:48
تأكد_يساوي(اشكال([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]), 3, "ثلاثة أشكال")
# apl-source:49
تأكد_يساوي(اشكال([[0]]), 0, "بلا جزر")
# apl-source:50
