
# apl-source:1
# مثال 1253 — إعادة بناء الطابور
# apl-source:2
# Queue reconstruction by height
# apl-source:3
# Demonstrates: ترتيب مخصص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1253-queue-reconstruction.apl
# apl-source:6

# apl-source:7
# نرتب بالطول تنازلياً ثم بالعدد تصاعدياً
# apl-source:8
# وندرج كل شخص عند فهرس عدده
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
def ابن_طابور(اشخاص):
  # apl-source:19
  ازواج = []
  # apl-source:20
  for ش in اشخاص:
    # apl-source:21
    ازواج = ازواج + [[-ش[0], ش[1]]]
  # apl-source:22
  ازواج = sorted(ازواج)
  # apl-source:23
  ناتج = []
  # apl-source:24
  for ز in ازواج:
    # apl-source:25
    ناتج.insert(ز[1], [-ز[0], ز[1]])
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(ابن_طابور([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]), [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]], "مثال أول")
# apl-source:29
تأكد_يساوي(ابن_طابور([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]), [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]], "مثال ثان")
# apl-source:30
