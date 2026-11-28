
# apl-source:1
# مثال 1340 — أطول مسار متزايد
# apl-source:2
# Longest increasing path in matrix
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1340-longest-increasing-path-matrix.apl
# apl-source:6

# apl-source:7
# نرتب الخلايا من الأصغر إلى الأكبر
# apl-source:8
# كل خلية تأخذ أفضل جار أصغر منها زائد واحد
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
def اطول_مسار(م):
  # apl-source:19
  ر_ = len(م)
  # apl-source:20
  ك_ = len(م[0])
  # apl-source:21
  خلايا = []
  # apl-source:22
  for ص in range(ر_):
    # apl-source:23
    for ج in range(ك_):
      # apl-source:24
      خلايا = خلايا + [[م[ص][ج], ص, ج]]
  # apl-source:25
  خلايا = sorted(خلايا)
  # apl-source:26
  بعد_ = []
  # apl-source:27
  for ع in range(ر_):
    # apl-source:28
    بعد_ = بعد_ + [[1] * ك_]
  # apl-source:29
  اقصى = 1
  # apl-source:30
  for خلية in خلايا:
    # apl-source:31
    ص = خلية[1]
    # apl-source:32
    ج = خلية[2]
    # apl-source:33
    for د in [[1,0],[-1,0],[0,1],[0,-1]]:
      # apl-source:34
      ر = ص + د[0]
      # apl-source:35
      ك = ج + د[1]
      # apl-source:36
      if (ر >= 0) and (ر < ر_) and (ك >= 0) and (ك < ك_):
        # apl-source:37
        if م[ر][ك] < م[ص][ج]:
          # apl-source:38
          if بعد_[ر][ك] + 1 > بعد_[ص][ج]:
            # apl-source:39
            بعد_[ص][ج] = بعد_[ر][ك] + 1
    # apl-source:40
    if بعد_[ص][ج] > اقصى:
      # apl-source:41
      اقصى = بعد_[ص][ج]
  # apl-source:42
  return اقصى
# apl-source:43

# apl-source:44
تأكد_يساوي(اطول_مسار([[9,9,4],[6,6,8],[2,1,1]]), 4, "أربعة")
# apl-source:45
تأكد_يساوي(اطول_مسار([[3,4,5],[3,2,6],[2,2,1]]), 4, "أربعة ثانية")
# apl-source:46
تأكد_يساوي(اطول_مسار([[1]]), 1, "خلية")
# apl-source:47
