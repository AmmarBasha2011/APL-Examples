
# apl-source:1
# مثال 1180 — أقل سهام
# apl-source:2
# Minimum arrows to burst balloons
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1180-min-arrows-balloons.apl
# apl-source:6

# apl-source:7
# نرتب بحسب النهاية
# apl-source:8
# وسهم واحد يفجر كل ما يبدأ قبل نهاية البالون الحالي
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
def اقل_سهام(نقاط):
  # apl-source:19
  if len(نقاط) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  ازواج = []
  # apl-source:22
  for ن in نقاط:
    # apl-source:23
    ازواج = ازواج + [[ن[1], ن[0]]]
  # apl-source:24
  ازواج = sorted(ازواج)
  # apl-source:25
  سهام = 1
  # apl-source:26
  نهاية = ازواج[0][0]
  # apl-source:27
  for ع in range(1, len(ازواج)):
    # apl-source:28
    if ازواج[ع][1] > نهاية:
      # apl-source:29
      سهام = سهام + 1
      # apl-source:30
      نهاية = ازواج[ع][0]
  # apl-source:31
  return سهام
# apl-source:32

# apl-source:33
تأكد_يساوي(اقل_سهام([[10,16],[2,8],[1,6],[7,12]]), 2, "مثال أول")
# apl-source:34
تأكد_يساوي(اقل_سهام([[1,2],[3,4],[5,6],[7,8]]), 4, "منفصلة")
# apl-source:35
تأكد_يساوي(اقل_سهام([[1,2],[2,3],[3,4],[4,5]]), 2, "متلامسة")
# apl-source:36
تأكد_يساوي(اقل_سهام([]), 0, "فارغة")
# apl-source:37
