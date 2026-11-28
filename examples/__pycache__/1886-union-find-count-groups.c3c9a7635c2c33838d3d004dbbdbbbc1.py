
# apl-source:1
# مثال 1886 — عدد المجموعات بالاتحاد والبحث
# apl-source:2
# Union find group count
# apl-source:3
# Demonstrates: رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1886-union-find-count-groups.apl
# apl-source:6

# apl-source:7
# نبحث عن جذر كل عنصر
# apl-source:8
# الدمج يقلل عدد المجموعات
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
    أب[ع] = أب[أب[ع]]
    # apl-source:21
    ع = أب[ع]
  # apl-source:22
  return ع
# apl-source:23

# apl-source:24
def عد_المجموعات(ن, أزواج):
  # apl-source:25
  أب = []
  # apl-source:26
  for ك in range(ن):
    # apl-source:27
    أب.append(ك)
  # apl-source:28
  عدد = ن
  # apl-source:29
  for ز in أزواج:
    # apl-source:30
    أ = جذر(أب, ز[0])
    # apl-source:31
    ب = جذر(أب, ز[1])
    # apl-source:32
    if أ != ب:
      # apl-source:33
      أب[أ] = ب
      # apl-source:34
      عدد = عدد - 1
  # apl-source:35
  return عدد
# apl-source:36

# apl-source:37
تأكد_يساوي(عد_المجموعات(5, [[0, 1], [1, 2], [3, 4]]), 2, "مجموعتان")
# apl-source:38
تأكد_يساوي(عد_المجموعات(3, []), 3, "منفصلة")
# apl-source:39
تأكد_يساوي(عد_المجموعات(4, [[0, 1], [1, 0]]), 3, "مكرر")
# apl-source:40
