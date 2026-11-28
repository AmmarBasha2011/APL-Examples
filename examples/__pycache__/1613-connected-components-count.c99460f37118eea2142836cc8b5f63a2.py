
# apl-source:1
# مثال 1613 — عدد المكونات المتصلة
# apl-source:2
# Count connected components
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1613-connected-components-count.apl
# apl-source:6

# apl-source:7
# نبدأ بحثاً من كل رأس لم نزره
# apl-source:8
# كل بحث جديد مكون جديد
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
def عدد_المكونات(ن, أضلاع):
  # apl-source:19
  جيران = {}
  # apl-source:20
  for ع in range(ن):
    # apl-source:21
    جيران[ع] = []
  # apl-source:22
  for ض in أضلاع:
    # apl-source:23
    جيران[ض[0]].append(ض[1])
    # apl-source:24
    جيران[ض[1]].append(ض[0])
  # apl-source:25
  زرنا = {}
  # apl-source:26
  مكونات = 0
  # apl-source:27
  for بداية in range(ن):
    # apl-source:28
    if بداية in زرنا:
      # apl-source:29
      مكونات = مكونات
    # apl-source:30
    else:
      # apl-source:31
      مكونات = مكونات + 1
      # apl-source:32
      مكدس = [بداية]
      # apl-source:33
      زرنا[بداية] = True
      # apl-source:34
      while len(مكدس) > 0:
        # apl-source:35
        ح = مكدس.pop()
        # apl-source:36
        for ج in جيران[ح]:
          # apl-source:37
          if ج in زرنا:
            # apl-source:38
            مكونات = مكونات
          # apl-source:39
          else:
            # apl-source:40
            زرنا[ج] = True
            # apl-source:41
            مكدس.append(ج)
  # apl-source:42
  return مكونات
# apl-source:43

# apl-source:44
تأكد_يساوي(عدد_المكونات(5, [[0, 1], [1, 2], [3, 4]]), 2, "مكونان")
# apl-source:45
تأكد_يساوي(عدد_المكونات(4, []), 4, "منعزلة")
# apl-source:46
تأكد_يساوي(عدد_المكونات(3, [[0, 1], [1, 2]]), 1, "مكون واحد")
# apl-source:47
