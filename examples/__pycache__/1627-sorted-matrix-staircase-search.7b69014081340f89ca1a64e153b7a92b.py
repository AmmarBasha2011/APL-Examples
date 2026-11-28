
# apl-source:1
# مثال 1627 — بحث الدرج في مصفوفة مرتبة
# apl-source:2
# Staircase search in sorted matrix
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1627-sorted-matrix-staircase-search.apl
# apl-source:6

# apl-source:7
# إن زاد العنصر عن الهدف نتحرك يساراً
# apl-source:8
# وإن نقص ننزل صفاً
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
def ابحث_في_المصفوفة(م, هدف):
  # apl-source:19
  ص = 0
  # apl-source:20
  ع = len(م[0]) - 1
  # apl-source:21
  while ص < len(م) and ع >= 0:
    # apl-source:22
    if م[ص][ع] == هدف:
      # apl-source:23
      return True
    # apl-source:24
    elif م[ص][ع] > هدف:
      # apl-source:25
      ع = ع - 1
    # apl-source:26
    else:
      # apl-source:27
      ص = ص + 1
  # apl-source:28
  return False
# apl-source:29

# apl-source:30
مصفوفة = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# apl-source:31
تأكد_يساوي(ابحث_في_المصفوفة(مصفوفة, 5), True, "موجود")
# apl-source:32
تأكد_يساوي(ابحث_في_المصفوفة(مصفوفة, 10), False, "غائب")
# apl-source:33
تأكد_يساوي(ابحث_في_المصفوفة(مصفوفة, 1), True, "الركن")
# apl-source:34
