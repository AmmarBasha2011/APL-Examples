
# apl-source:1
# مثال 1383 — أفضل زوج معالم
# apl-source:2
# Best sightseeing pair
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1383-best-sightseeing-pair.apl
# apl-source:6

# apl-source:7
# القيمة قيمة i زائد قيمة j زائد i ناقص j
# apl-source:8
# نحتفظ بأفضل قيمة i زائد الموضع
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
def افضل_زوج(قيم):
  # apl-source:19
  افضل_بداية = قيم[0]
  # apl-source:20
  افضل = 0
  # apl-source:21
  for ي in range(1, len(قيم)):
    # apl-source:22
    مجموع = افضل_بداية + قيم[ي] - ي
    # apl-source:23
    if مجموع > افضل:
      # apl-source:24
      افضل = مجموع
    # apl-source:25
    if قيم[ي] + ي > افضل_بداية:
      # apl-source:26
      افضل_بداية = قيم[ي] + ي
  # apl-source:27
  return افضل
# apl-source:28

# apl-source:29
تأكد_يساوي(افضل_زوج([8,1,5,2,6]), 11, "أحد عشر")
# apl-source:30
تأكد_يساوي(افضل_زوج([1,2]), 2, "عنصران")
# apl-source:31
تأكد_يساوي(افضل_زوج([5,5,5]), 9, "متساوية")
# apl-source:32
