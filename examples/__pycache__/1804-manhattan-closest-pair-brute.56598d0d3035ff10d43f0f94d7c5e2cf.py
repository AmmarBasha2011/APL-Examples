
# apl-source:1
# مثال 1804 — أقرب نقطتين بمسافة مانهاتن
# apl-source:2
# Closest pair by Manhattan distance
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1804-manhattan-closest-pair-brute.apl
# apl-source:6

# apl-source:7
# المسافة مجموع الفروق المطلقة
# apl-source:8
# نحتفظ بالأصغر
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
def مسافة(أ, ب):
  # apl-source:19
  س = أ[0] - ب[0]
  # apl-source:20
  ص = أ[1] - ب[1]
  # apl-source:21
  if س < 0:
    # apl-source:22
    س = -س
  # apl-source:23
  if ص < 0:
    # apl-source:24
    ص = -ص
  # apl-source:25
  return س + ص
# apl-source:26

# apl-source:27
def أقرب_زوج(نقاط):
  # apl-source:28
  أفضل = 1000000
  # apl-source:29
  for ي in range(len(نقاط)):
    # apl-source:30
    for ك in range(ي + 1, len(نقاط)):
      # apl-source:31
      أفضل = min(أفضل, مسافة(نقاط[ي], نقاط[ك]))
  # apl-source:32
  return أفضل
# apl-source:33

# apl-source:34
تأكد_يساوي(أقرب_زوج([[0, 0], [5, 5], [1, 1]]), 2, "ثلاث")
# apl-source:35
تأكد_يساوي(أقرب_زوج([[0, 0], [0, 1]]), 1, "اثنتان")
# apl-source:36
