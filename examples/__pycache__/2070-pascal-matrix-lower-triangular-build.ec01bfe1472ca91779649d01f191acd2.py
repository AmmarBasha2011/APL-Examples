
# apl-source:1
# مثال 2070 — مصفوفة باسكال السفلية
# apl-source:2
# Pascal lower triangular matrix
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2070-pascal-matrix-lower-triangular-build.apl
# apl-source:6

# apl-source:7
# # كل عنصر مجموع ما فوقه وما على يساره العلوي
# apl-source:8
# # العناصر فوق القطر أصفار
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
def باسكال(ن):
  # apl-source:19
  م = []
  # apl-source:20
  for ي in range(ن):
    # apl-source:21
    صف = [0] * ن
    # apl-source:22
    صف[0] = 1
    # apl-source:23
    for ك in range(1, ي + 1):
      # apl-source:24
      صف[ك] = م[ي - 1][ك - 1] + م[ي - 1][ك]
    # apl-source:25
    م = م + [صف]
  # apl-source:26
  return م
# apl-source:27

# apl-source:28
تأكد_يساوي(باسكال(4), [[1, 0, 0, 0], [1, 1, 0, 0], [1, 2, 1, 0], [1, 3, 3, 1]], "٤×٤")
# apl-source:29
تأكد_يساوي(باسكال(1), [[1]], "١×١")
# apl-source:30
