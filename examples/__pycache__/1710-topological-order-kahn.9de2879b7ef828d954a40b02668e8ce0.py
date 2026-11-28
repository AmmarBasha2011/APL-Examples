
# apl-source:1
# مثال 1710 — ترتيب طوبولوجي بطريقة كان
# apl-source:2
# Topological order by Kahn
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1710-topological-order-kahn.apl
# apl-source:6

# apl-source:7
# نحسب درجة الدخول
# apl-source:8
# نخفضها عند إزالة كل عقدة
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
def ترتيب_طوبولوجي(ن, حواف):
  # apl-source:19
  درجة = []
  # apl-source:20
  جيران = []
  # apl-source:21
  for ك in range(ن):
    # apl-source:22
    درجة.append(0)
    # apl-source:23
    جيران.append([])
  # apl-source:24
  for ح in حواف:
    # apl-source:25
    جيران[ح[0]].append(ح[1])
    # apl-source:26
    درجة[ح[1]] = درجة[ح[1]] + 1
  # apl-source:27
  طابور = []
  # apl-source:28
  for ك in range(ن):
    # apl-source:29
    if درجة[ك] == 0:
      # apl-source:30
      طابور.append(ك)
  # apl-source:31
  ناتج = []
  # apl-source:32
  while len(طابور) > 0:
    # apl-source:33
    ع = طابور.pop(0)
    # apl-source:34
    ناتج.append(ع)
    # apl-source:35
    for ج in جيران[ع]:
      # apl-source:36
      درجة[ج] = درجة[ج] - 1
      # apl-source:37
      if درجة[ج] == 0:
        # apl-source:38
        طابور.append(ج)
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
تأكد_يساوي(ترتيب_طوبولوجي(4, [[0, 1], [0, 2], [1, 3], [2, 3]]), [0, 1, 2, 3], "ماسة")
# apl-source:42
تأكد_يساوي(len(ترتيب_طوبولوجي(2, [[0, 1], [1, 0]])), 0, "دورة")
# apl-source:43
