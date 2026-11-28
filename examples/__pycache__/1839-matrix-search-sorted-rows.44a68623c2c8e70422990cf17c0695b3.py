
# apl-source:1
# مثال 1839 — البحث في مصفوفة مرتبة
# apl-source:2
# Search in row-column sorted matrix
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1839-matrix-search-sorted-rows.apl
# apl-source:6

# apl-source:7
# أكبر من الهدف نذهب يساراً
# apl-source:8
# أصغر منه ننزل
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
def ابحث_مصفوفة(م, هدف):
  # apl-source:19
  ي = 0
  # apl-source:20
  ك = len(م[0]) - 1
  # apl-source:21
  while ي < len(م) and ك >= 0:
    # apl-source:22
    if م[ي][ك] == هدف:
      # apl-source:23
      return True
    # apl-source:24
    if م[ي][ك] > هدف:
      # apl-source:25
      ك = ك - 1
    # apl-source:26
    else:
      # apl-source:27
      ي = ي + 1
  # apl-source:28
  return False
# apl-source:29

# apl-source:30
م = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# apl-source:31
تأكد_يساوي(ابحث_مصفوفة(م, 5), True, "وسط")
# apl-source:32
تأكد_يساوي(ابحث_مصفوفة(م, 10), False, "غائب")
# apl-source:33
تأكد_يساوي(ابحث_مصفوفة(م, 3), True, "زاوية")
# apl-source:34
