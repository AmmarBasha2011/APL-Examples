
# apl-source:1
# مثال 1712 — عدد المكونات المتصلة
# apl-source:2
# Count connected components
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1712-graph-components-dfs-total.apl
# apl-source:6

# apl-source:7
# نبدأ بحثاً جديداً لكل مكون
# apl-source:8
# نعد مرات البدء
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
def عد_المكونات(ن, حواف):
  # apl-source:19
  جيران = []
  # apl-source:20
  for ك in range(ن):
    # apl-source:21
    جيران.append([])
  # apl-source:22
  for ح in حواف:
    # apl-source:23
    جيران[ح[0]].append(ح[1])
    # apl-source:24
    جيران[ح[1]].append(ح[0])
  # apl-source:25
  زار = []
  # apl-source:26
  for ك in range(ن):
    # apl-source:27
    زار.append(False)
  # apl-source:28
  عد = 0
  # apl-source:29
  for بداية in range(ن):
    # apl-source:30
    if زار[بداية] == False:
      # apl-source:31
      عد = عد + 1
      # apl-source:32
      زار[بداية] = True
      # apl-source:33
      مكدس = [بداية]
      # apl-source:34
      while len(مكدس) > 0:
        # apl-source:35
        ع = مكدس.pop()
        # apl-source:36
        for ج in جيران[ع]:
          # apl-source:37
          if زار[ج] == False:
            # apl-source:38
            زار[ج] = True
            # apl-source:39
            مكدس.append(ج)
  # apl-source:40
  return عد
# apl-source:41

# apl-source:42
تأكد_يساوي(عد_المكونات(5, [[0, 1], [1, 2], [3, 4]]), 2, "اثنان")
# apl-source:43
تأكد_يساوي(عد_المكونات(3, []), 3, "منفصلة")
# apl-source:44
تأكد_يساوي(عد_المكونات(4, [[0, 1], [1, 2], [2, 3]]), 1, "سلسلة")
# apl-source:45
