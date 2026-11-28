
# apl-source:1
# مثال 1612 — مصفوفة الجوار من الأضلاع
# apl-source:2
# Adjacency matrix from edges
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1612-adjacency-matrix-from-edges.apl
# apl-source:6

# apl-source:7
# نبني مصفوفة أصفار
# apl-source:8
# نضع واحداً في الموضعين لكل ضلع
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
def مصفوفة_الجوار(ن, أضلاع):
  # apl-source:19
  م = []
  # apl-source:20
  for ص in range(ن):
    # apl-source:21
    صف = []
    # apl-source:22
    for ع in range(ن):
      # apl-source:23
      صف.append(0)
    # apl-source:24
    م.append(صف)
  # apl-source:25
  for ض in أضلاع:
    # apl-source:26
    م[ض[0]][ض[1]] = 1
    # apl-source:27
    م[ض[1]][ض[0]] = 1
  # apl-source:28
  return م
# apl-source:29

# apl-source:30
تأكد_يساوي(مصفوفة_الجوار(3, [[0, 1], [1, 2]]), [[0, 1, 0], [1, 0, 1], [0, 1, 0]], "مسار")
# apl-source:31
تأكد_يساوي(مصفوفة_الجوار(2, []), [[0, 0], [0, 0]], "بلا أضلاع")
# apl-source:32
