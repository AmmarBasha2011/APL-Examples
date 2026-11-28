
# apl-source:1
# مثال 1883 — قطر الشجرة
# apl-source:2
# Tree diameter by BFS twice
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1883-tree-diameter-parents-path.apl
# apl-source:6

# apl-source:7
# نبحث عن أبعد عقدة من أي بداية
# apl-source:8
# ثم أبعد عقدة منها
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
def أبعد(جيران, بداية):
  # apl-source:19
  مسافة = {}
  # apl-source:20
  مسافة[str(بداية)] = 0
  # apl-source:21
  طابور = [بداية]
  # apl-source:22
  أفضل = بداية
  # apl-source:23
  while len(طابور) > 0:
    # apl-source:24
    ع = طابور.pop(0)
    # apl-source:25
    for ج in جيران[ع]:
      # apl-source:26
      if (str(ج) in مسافة) == False:
        # apl-source:27
        مسافة[str(ج)] = مسافة[str(ع)] + 1
        # apl-source:28
        طابور.append(ج)
        # apl-source:29
        if مسافة[str(ج)] > مسافة[str(أفضل)]:
          # apl-source:30
          أفضل = ج
  # apl-source:31
  return [أفضل, مسافة[str(أفضل)]]
# apl-source:32

# apl-source:33
def قطر(ن, حواف):
  # apl-source:34
  جيران = []
  # apl-source:35
  for ك in range(ن):
    # apl-source:36
    جيران.append([])
  # apl-source:37
  for ح in حواف:
    # apl-source:38
    جيران[ح[0]].append(ح[1])
    # apl-source:39
    جيران[ح[1]].append(ح[0])
  # apl-source:40
  أول = أبعد(جيران, 0)
  # apl-source:41
  return أبعد(جيران, أول[0])[1]
# apl-source:42

# apl-source:43
تأكد_يساوي(قطر(5, [[0, 1], [1, 2], [2, 3], [1, 4]]), 3, "خمس عقد")
# apl-source:44
تأكد_يساوي(قطر(2, [[0, 1]]), 1, "عقدتان")
# apl-source:45
تأكد_يساوي(قطر(4, [[0, 1], [0, 2], [0, 3]]), 2, "نجمة")
# apl-source:46
