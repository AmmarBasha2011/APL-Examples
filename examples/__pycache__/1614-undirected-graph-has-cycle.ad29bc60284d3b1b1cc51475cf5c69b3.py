
# apl-source:1
# مثال 1614 — دورة في رسم غير موجه
# apl-source:2
# Cycle detection in undirected graph
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1614-undirected-graph-has-cycle.apl
# apl-source:6

# apl-source:7
# بحث عميق مع تتبع الأب
# apl-source:8
# جار مزور غير الأب يعني دورة
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
def فيه_دورة(ن, أضلاع):
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
  for بداية in range(ن):
    # apl-source:27
    if بداية in زرنا:
      # apl-source:28
      زرنا = زرنا
    # apl-source:29
    else:
      # apl-source:30
      زرنا[بداية] = True
      # apl-source:31
      مكدس = [[بداية, -1]]
      # apl-source:32
      while len(مكدس) > 0:
        # apl-source:33
        ح = مكدس.pop()
        # apl-source:34
        for ج in جيران[ح[0]]:
          # apl-source:35
          if ج == ح[1]:
            # apl-source:36
            زرنا = زرنا
          # apl-source:37
          elif ج in زرنا:
            # apl-source:38
            return True
          # apl-source:39
          else:
            # apl-source:40
            زرنا[ج] = True
            # apl-source:41
            مكدس.append([ج, ح[0]])
  # apl-source:42
  return False
# apl-source:43

# apl-source:44
تأكد_يساوي(فيه_دورة(3, [[0, 1], [1, 2], [2, 0]]), True, "مثلث")
# apl-source:45
تأكد_يساوي(فيه_دورة(4, [[0, 1], [1, 2], [2, 3]]), False, "مسار")
# apl-source:46
تأكد_يساوي(فيه_دورة(2, []), False, "بلا أضلاع")
# apl-source:47
