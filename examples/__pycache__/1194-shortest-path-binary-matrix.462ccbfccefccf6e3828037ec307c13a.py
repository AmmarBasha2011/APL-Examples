
# apl-source:1
# مثال 1194 — أقصر مسار في شبكة
# apl-source:2
# Shortest path in binary matrix
# apl-source:3
# Demonstrates: بحث بالعرض
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1194-shortest-path-binary-matrix.apl
# apl-source:6

# apl-source:7
# نبدأ من الزاوية العليا اليسرى
# apl-source:8
# ونتقدم بالعرض في ثمانية اتجاهات عبر الخانات الصفرية
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
def اقصر_مسار(ش):
  # apl-source:19
  ن = len(ش)
  # apl-source:20
  if (ش[0][0] == 1) or (ش[ن - 1][ن - 1] == 1):
    # apl-source:21
    return -1
  # apl-source:22
  مرئي = []
  # apl-source:23
  for ك0 in range(ن):
    # apl-source:24
    مرئي = مرئي + [[False] * ن]
  # apl-source:25
  طابور = [[0, 0, 1]]
  # apl-source:26
  مرئي[0][0] = True
  # apl-source:27
  ع = 0
  # apl-source:28
  while ع < len(طابور):
    # apl-source:29
    ص = طابور[ع][0]
    # apl-source:30
    ج = طابور[ع][1]
    # apl-source:31
    مسافة = طابور[ع][2]
    # apl-source:32
    ع = ع + 1
    # apl-source:33
    if (ص == ن - 1) and (ج == ن - 1):
      # apl-source:34
      return مسافة
    # apl-source:35
    for د1 in [-1, 0, 1]:
      # apl-source:36
      for د2 in [-1, 0, 1]:
        # apl-source:37
        ر = ص + د1
        # apl-source:38
        ك = ج + د2
        # apl-source:39
        if (ر >= 0) and (ر < ن) and (ك >= 0) and (ك < ن):
          # apl-source:40
          if (ش[ر][ك] == 0) and (not مرئي[ر][ك]):
            # apl-source:41
            مرئي[ر][ك] = True
            # apl-source:42
            طابور = طابور + [[ر, ك, مسافة + 1]]
  # apl-source:43
  return -1
# apl-source:44

# apl-source:45
تأكد_يساوي(اقصر_مسار([[0,1],[1,0]]), 2, "قطري")
# apl-source:46
تأكد_يساوي(اقصر_مسار([[0,0,0],[1,1,0],[1,1,0]]), 4, "ثلاثة في ثلاثة")
# apl-source:47
تأكد_يساوي(اقصر_مسار([[1,0,0],[1,1,0],[1,1,0]]), -1, "بداية مسدودة")
# apl-source:48
تأكد_يساوي(اقصر_مسار([[0]]), 1, "خانة واحدة")
# apl-source:49
