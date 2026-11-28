
# apl-source:1
# مثال 1884 — أقصر مسافة بخوارزمية ديكسترا
# apl-source:2
# Dijkstra shortest distance
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1884-dijkstra-small-graph-distance.apl
# apl-source:6

# apl-source:7
# مصفوفة مسافات تبدأ لانهائية
# apl-source:8
# نحدث الجيران بعد كل اختيار
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
def ديكسترا(ن, حواف, بداية):
  # apl-source:19
  كبير = 1000000
  # apl-source:20
  مسافة = []
  # apl-source:21
  زار = []
  # apl-source:22
  for ك in range(ن):
    # apl-source:23
    مسافة.append(كبير)
    # apl-source:24
    زار.append(False)
  # apl-source:25
  مسافة[بداية] = 0
  # apl-source:26
  for خطوة in range(ن):
    # apl-source:27
    ع = -1
    # apl-source:28
    for ك in range(ن):
      # apl-source:29
      if زار[ك] == False and (ع == -1 or مسافة[ك] < مسافة[ع]):
        # apl-source:30
        ع = ك
    # apl-source:31
    if ع == -1 or مسافة[ع] == كبير:
      # apl-source:32
      return مسافة
    # apl-source:33
    زار[ع] = True
    # apl-source:34
    for ح in حواف:
      # apl-source:35
      if ح[0] == ع and مسافة[ع] + ح[2] < مسافة[ح[1]]:
        # apl-source:36
        مسافة[ح[1]] = مسافة[ع] + ح[2]
  # apl-source:37
  return مسافة
# apl-source:38

# apl-source:39
ح = [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5]]
# apl-source:40
تأكد_يساوي(ديكسترا(4, ح, 0), [0, 3, 1, 4], "أربع عقد")
# apl-source:41
تأكد_يساوي(ديكسترا(2, [], 0)[1], 1000000, "غير متصل")
# apl-source:42
