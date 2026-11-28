
# apl-source:1
# مثال 1381 — شرائح حسابية
# apl-source:2
# Arithmetic slices count
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1381-arithmetic-slices-count.apl
# apl-source:6

# apl-source:7
# كل عنصر يمد شريحة حسابية بنفس الفارق
# apl-source:8
# نجمع ما ينتهي عند كل موضع
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
def عد_شرائح(أرقام):
  # apl-source:19
  حالي = 0
  # apl-source:20
  مجموع = 0
  # apl-source:21
  for ع in range(2, len(أرقام)):
    # apl-source:22
    if أرقام[ع] - أرقام[ع - 1] == أرقام[ع - 1] - أرقام[ع - 2]:
      # apl-source:23
      حالي = حالي + 1
      # apl-source:24
      مجموع = مجموع + حالي
    # apl-source:25
    else:
      # apl-source:26
      حالي = 0
  # apl-source:27
  return مجموع
# apl-source:28

# apl-source:29
تأكد_يساوي(عد_شرائح([1,2,3,4]), 3, "ثلاث")
# apl-source:30
تأكد_يساوي(عد_شرائح([1]), 0, "عنصر")
# apl-source:31
تأكد_يساوي(عد_شرائح([1,3,5,7,9]), 6, "ست")
# apl-source:32
