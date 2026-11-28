
# apl-source:1
# مثال 1330 — لعبة الزنزانة
# apl-source:2
# Dungeon game minimum health
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1330-dungeon-game.apl
# apl-source:6

# apl-source:7
# نحسب من النهاية إلى البداية
# apl-source:8
# الصحة يجب ألا تقل عن واحد
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
def صحة_دنيا(م):
  # apl-source:19
  ر_ = len(م)
  # apl-source:20
  ك_ = len(م[0])
  # apl-source:21
  د = []
  # apl-source:22
  for ع in range(ر_):
    # apl-source:23
    د = د + [[0] * ك_]
  # apl-source:24
  for ع in range(ر_ - 1, -1, -1):
    # apl-source:25
    for ج in range(ك_ - 1, -1, -1):
      # apl-source:26
      if (ع == ر_ - 1) and (ج == ك_ - 1):
        # apl-source:27
        د[ع][ج] = max(1, 1 - م[ع][ج])
      # apl-source:28
      elif ع == ر_ - 1:
        # apl-source:29
        د[ع][ج] = max(1, د[ع][ج + 1] - م[ع][ج])
      # apl-source:30
      elif ج == ك_ - 1:
        # apl-source:31
        د[ع][ج] = max(1, د[ع + 1][ج] - م[ع][ج])
      # apl-source:32
      else:
        # apl-source:33
        د[ع][ج] = max(1, min(د[ع + 1][ج], د[ع][ج + 1]) - م[ع][ج])
  # apl-source:34
  return د[0][0]
# apl-source:35

# apl-source:36
تأكد_يساوي(صحة_دنيا([[-2,-3,3],[-5,-10,1],[10,30,-5]]), 7, "مثال أول")
# apl-source:37
تأكد_يساوي(صحة_دنيا([[0]]), 1, "خلية")
# apl-source:38
تأكد_يساوي(صحة_دنيا([[100]]), 1, "موجبة")
# apl-source:39
