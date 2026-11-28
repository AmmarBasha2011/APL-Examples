
# apl-source:1
# مثال 1887 — الحافة الزائدة في الرسم
# apl-source:2
# Find redundant edge forming cycle
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1887-redundant-edge-cycle-detect.apl
# apl-source:6

# apl-source:7
# نستخدم الاتحاد والبحث
# apl-source:8
# الحافة التي تربط جذراً واحداً تشكل دورة
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
def زائدة(ن, حواف):
  # apl-source:24
  أب = []
  # apl-source:25
  for ك in range(ن + 1):
    # apl-source:26
    أب.append(ك)
  # apl-source:27
  for ح in حواف:
    # apl-source:28
    أ = جذر(أب, ح[0])
    # apl-source:29
    ب = جذر(أب, ح[1])
    # apl-source:30
    if أ == ب:
      # apl-source:31
      return ح
    # apl-source:32
    أب[أ] = ب
  # apl-source:33
  return []
# apl-source:34

# apl-source:35
تأكد_يساوي(زائدة(3, [[1, 2], [1, 3], [2, 3]]), [2, 3], "مثلث")
# apl-source:36
تأكد_يساوي(زائدة(3, [[1, 2], [2, 3]]), [], "بلا دورة")
# apl-source:37
تأكد_يساوي(زائدة(4, [[1, 2], [2, 3], [3, 4], [1, 4]]), [1, 4], "مربع")
# apl-source:38
