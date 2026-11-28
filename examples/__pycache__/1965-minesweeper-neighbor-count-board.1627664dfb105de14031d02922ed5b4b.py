
# apl-source:1
# مثال 1965 — أرقام لوحة كاسحة الألغام
# apl-source:2
# Minesweeper neighbor counts
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1965-minesweeper-neighbor-count-board.apl
# apl-source:6

# apl-source:7
# # نفحص الجيران ضمن حدود اللوحة
# apl-source:8
# # الخلية التي فيها لغم تبقى *
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
def لوحة(الغام, ص, س):
  # apl-source:19
  لغم = {}
  # apl-source:20
  for ل in الغام:
    # apl-source:21
    لغم[str(ل[0]) + "," + str(ل[1])] = 1
  # apl-source:22
  خرج = []
  # apl-source:23
  for ي in range(ص):
    # apl-source:24
    صف = ""
    # apl-source:25
    for ك in range(س):
      # apl-source:26
      if (str(ي) + "," + str(ك)) in لغم:
        # apl-source:27
        صف = صف + "*"
      # apl-source:28
      else:
        # apl-source:29
        عد = 0
        # apl-source:30
        for د1 in [-1, 0, 1]:
          # apl-source:31
          for د2 in [-1, 0, 1]:
            # apl-source:32
            if (د1 != 0 or د2 != 0) and ((str(ي + د1) + "," + str(ك + د2)) in لغم):
              # apl-source:33
              عد = عد + 1
        # apl-source:34
        صف = صف + str(عد)
    # apl-source:35
    خرج = خرج + [صف]
  # apl-source:36
  return خرج
# apl-source:37

# apl-source:38
تأكد_يساوي(لوحة([[0, 0], [2, 2]], 3, 3), ["*1.".replace(".", "0"), "121", "01*"], "لغمان")
# apl-source:39
تأكد_يساوي(لوحة([], 2, 2), ["00", "00"], "بلا ألغام")
# apl-source:40
