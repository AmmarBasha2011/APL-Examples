
# apl-source:1
# مثال 1707 — أقصر مسار في شبكة بالعرض أولاً
# apl-source:2
# Shortest grid path steps by BFS
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1707-grid-shortest-path-bfs-steps.apl
# apl-source:6

# apl-source:7
# الطابور يحمل الموضع والمسافة
# apl-source:8
# الجدران قيمتها واحد
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
def أقصر_مسار(شبكة):
  # apl-source:19
  ص = len(شبكة)
  # apl-source:20
  س = len(شبكة[0])
  # apl-source:21
  رأينا = {}
  # apl-source:22
  طابور = [[0, 0, 0]]
  # apl-source:23
  رأينا["0,0"] = 1
  # apl-source:24
  اتجاهات = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  # apl-source:25
  while len(طابور) > 0:
    # apl-source:26
    ح = طابور.pop(0)
    # apl-source:27
    if ح[0] == ص - 1 and ح[1] == س - 1:
      # apl-source:28
      return ح[2]
    # apl-source:29
    for ا in اتجاهات:
      # apl-source:30
      ي = ح[0] + ا[0]
      # apl-source:31
      ك = ح[1] + ا[1]
      # apl-source:32
      if ي >= 0 and ي < ص and ك >= 0 and ك < س:
        # apl-source:33
        if شبكة[ي][ك] == 0:
          # apl-source:34
          مفتاح = str(ي) + "," + str(ك)
          # apl-source:35
          if (مفتاح in رأينا) == False:
            # apl-source:36
            رأينا[مفتاح] = 1
            # apl-source:37
            طابور.append([ي, ك, ح[2] + 1])
  # apl-source:38
  return -1
# apl-source:39

# apl-source:40
تأكد_يساوي(أقصر_مسار([[0, 0, 0], [1, 1, 0], [0, 0, 0]]), 4, "التفاف")
# apl-source:41
تأكد_يساوي(أقصر_مسار([[0, 1], [1, 0]]), -1, "مسدود")
# apl-source:42
تأكد_يساوي(أقصر_مسار([[0]]), 0, "خلية")
# apl-source:43
