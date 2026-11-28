
# apl-source:1
# مثال 1347 — تقسيم ممكن
# apl-source:2
# Possible bipartition of dislikes
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1347-possible-bipartition.apl
# apl-source:6

# apl-source:7
# كل زوج متنافر حافة
# apl-source:8
# نلون الرسم بلونين بالبحث بالعرض
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
def تقسيم_ممكن(ن, تنافر):
  # apl-source:19
  جيران = []
  # apl-source:20
  for ع in range(ن + 1):
    # apl-source:21
    جيران = جيران + [[]]
  # apl-source:22
  for ز in تنافر:
    # apl-source:23
    جيران[ز[0]] = جيران[ز[0]] + [ز[1]]
    # apl-source:24
    جيران[ز[1]] = جيران[ز[1]] + [ز[0]]
  # apl-source:25
  لون = [0] * (ن + 1)
  # apl-source:26
  for بداية in range(1, ن + 1):
    # apl-source:27
    if لون[بداية] == 0:
      # apl-source:28
      لون[بداية] = 1
      # apl-source:29
      طابور = [بداية]
      # apl-source:30
      ع = 0
      # apl-source:31
      while ع < len(طابور):
        # apl-source:32
        ق = طابور[ع]
        # apl-source:33
        ع = ع + 1
        # apl-source:34
        for ج in جيران[ق]:
          # apl-source:35
          if لون[ج] == 0:
            # apl-source:36
            لون[ج] = -لون[ق]
            # apl-source:37
            طابور = طابور + [ج]
          # apl-source:38
          elif لون[ج] == لون[ق]:
            # apl-source:39
            return False
  # apl-source:40
  return True
# apl-source:41

# apl-source:42
تأكد_يساوي(تقسيم_ممكن(4, [[1,2],[1,3],[2,4]]), True, "ممكن")
# apl-source:43
تأكد_يساوي(تقسيم_ممكن(3, [[1,2],[1,3],[2,3]]), False, "مثلث")
# apl-source:44
تأكد_يساوي(تقسيم_ممكن(2, []), True, "بلا تنافر")
# apl-source:45
