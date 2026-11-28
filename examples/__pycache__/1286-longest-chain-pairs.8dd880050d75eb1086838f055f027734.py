
# apl-source:1
# مثال 1286 — أطول سلسلة أزواج
# apl-source:2
# Longest chain of pairs
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1286-longest-chain-pairs.apl
# apl-source:6

# apl-source:7
# نرتب الأزواج بالعنصر الثاني
# apl-source:8
# ونأخذ كل زوج يبدأ بعد نهاية السابق
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
def سلسلة(ازواج):
  # apl-source:19
  ق = []
  # apl-source:20
  for ز in ازواج:
    # apl-source:21
    ق = ق + [[ز[1], ز[0]]]
  # apl-source:22
  ق = sorted(ق)
  # apl-source:23
  نهاية = -10 ** 9
  # apl-source:24
  ع = 0
  # apl-source:25
  for ز in ق:
    # apl-source:26
    if ز[1] > نهاية:
      # apl-source:27
      ع = ع + 1
      # apl-source:28
      نهاية = ز[0]
  # apl-source:29
  return ع
# apl-source:30

# apl-source:31
تأكد_يساوي(سلسلة([[1,2],[2,3],[3,4]]), 2, "مثال أول")
# apl-source:32
تأكد_يساوي(سلسلة([[1,2],[7,8],[4,5]]), 3, "كلها")
# apl-source:33
تأكد_يساوي(سلسلة([[1,10],[2,3],[4,5]]), 2, "ازدحام")
# apl-source:34
تأكد_يساوي(سلسلة([]), 0, "فارغة")
# apl-source:35
