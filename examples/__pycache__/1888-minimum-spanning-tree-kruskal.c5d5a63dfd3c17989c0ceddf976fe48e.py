
# apl-source:1
# مثال 1888 — أقل شجرة ممتدة بكروسكال
# apl-source:2
# Kruskal minimum spanning tree weight
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1888-minimum-spanning-tree-kruskal.apl
# apl-source:6

# apl-source:7
# نرتب الحواف بالوزن
# apl-source:8
# نتجنب الدورات بالاتحاد
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
def جذر(أب, ع):
  # apl-source:19
  while أب[ع] != ع:
    # apl-source:20
    ع = أب[ع]
  # apl-source:21
  return ع
# apl-source:22

# apl-source:23
def كروسكال(ن, حواف):
  # apl-source:24
  مرتبة = []
  # apl-source:25
  for ح in حواف:
    # apl-source:26
    مرتبة.append([ح[2], ح[0], ح[1]])
  # apl-source:27
  مرتبة.sort()
  # apl-source:28
  أب = []
  # apl-source:29
  for ك in range(ن):
    # apl-source:30
    أب.append(ك)
  # apl-source:31
  مجموع = 0
  # apl-source:32
  for ح in مرتبة:
    # apl-source:33
    أ = جذر(أب, ح[1])
    # apl-source:34
    ب = جذر(أب, ح[2])
    # apl-source:35
    if أ != ب:
      # apl-source:36
      أب[أ] = ب
      # apl-source:37
      مجموع = مجموع + ح[0]
  # apl-source:38
  return مجموع
# apl-source:39

# apl-source:40
ح = [[0, 1, 1], [1, 2, 2], [0, 2, 3], [2, 3, 4], [1, 3, 5]]
# apl-source:41
تأكد_يساوي(كروسكال(4, ح), 7, "أربع عقد")
# apl-source:42
تأكد_يساوي(كروسكال(2, [[0, 1, 9]]), 9, "حافة")
# apl-source:43
