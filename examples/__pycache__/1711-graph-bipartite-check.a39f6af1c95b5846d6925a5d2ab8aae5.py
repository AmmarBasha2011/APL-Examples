
# apl-source:1
# مثال 1711 — هل الرسم ثنائي التجزئة
# apl-source:2
# Bipartite graph check
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1711-graph-bipartite-check.apl
# apl-source:6

# apl-source:7
# نلون الجار بعكس اللون
# apl-source:8
# التعارض يعني فشلاً
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
def ثنائي(جيران):
  # apl-source:19
  ن = len(جيران)
  # apl-source:20
  لون = []
  # apl-source:21
  for ك in range(ن):
    # apl-source:22
    لون.append(-1)
  # apl-source:23
  for بداية in range(ن):
    # apl-source:24
    if لون[بداية] == -1:
      # apl-source:25
      لون[بداية] = 0
      # apl-source:26
      طابور = [بداية]
      # apl-source:27
      while len(طابور) > 0:
        # apl-source:28
        ع = طابور.pop(0)
        # apl-source:29
        for ج in جيران[ع]:
          # apl-source:30
          if لون[ج] == -1:
            # apl-source:31
            لون[ج] = 1 - لون[ع]
            # apl-source:32
            طابور.append(ج)
          # apl-source:33
          elif لون[ج] == لون[ع]:
            # apl-source:34
            return False
  # apl-source:35
  return True
# apl-source:36

# apl-source:37
تأكد_يساوي(ثنائي([[1, 3], [0, 2], [1, 3], [0, 2]]), True, "مربع")
# apl-source:38
تأكد_يساوي(ثنائي([[1, 2], [0, 2], [0, 1]]), False, "مثلث")
# apl-source:39
