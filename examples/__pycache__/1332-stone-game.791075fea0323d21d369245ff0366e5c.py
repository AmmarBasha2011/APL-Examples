
# apl-source:1
# مثال 1332 — لعبة الحجارة
# apl-source:2
# Stone game optimal play
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1332-stone-game.apl
# apl-source:6

# apl-source:7
# كل لاعب يأخذ من أحد طرفي الصف
# apl-source:8
# نخزن أفضل فارق لكل مجال
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
def فارق_الأول(أكوام):
  # apl-source:19
  ن = len(أكوام)
  # apl-source:20
  فارق = []
  # apl-source:21
  for ع in range(ن):
    # apl-source:22
    فارق = فارق + [[0] * ن]
  # apl-source:23
  for ع in range(ن):
    # apl-source:24
    فارق[ع][ع] = أكوام[ع]
  # apl-source:25
  for ط in range(2, ن + 1):
    # apl-source:26
    for ي in range(0, ن - ط + 1):
      # apl-source:27
      ك = ي + ط - 1
      # apl-source:28
      فارق[ي][ك] = max(أكوام[ي] - فارق[ي + 1][ك], أكوام[ك] - فارق[ي][ك - 1])
  # apl-source:29
  return فارق[0][ن - 1]
# apl-source:30

# apl-source:31
تأكد_يساوي(فارق_الأول([5,3,4,5]), 1, "فارق واحد")
# apl-source:32
تأكد_يساوي(فارق_الأول([3,7,2,3]), 5, "فارق خمسة")
# apl-source:33
تأكد_يساوي(فارق_الأول([4]), 4, "كومة")
# apl-source:34
