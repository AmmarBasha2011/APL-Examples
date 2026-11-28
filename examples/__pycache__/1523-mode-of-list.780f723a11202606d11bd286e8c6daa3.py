
# apl-source:1
# مثال 1523 — المنوال
# apl-source:2
# Mode of a list
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1523-mode-of-list.apl
# apl-source:6

# apl-source:7
# نعد تكرار كل قيمة
# apl-source:8
# عند التعادل نأخذ الأصغر
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
def المنوال(أ):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ع in أ:
    # apl-source:21
    عد[ع] = عد.get(ع, 0) + 1
  # apl-source:22
  أفضل = أ[0]
  # apl-source:23
  for ع in أ:
    # apl-source:24
    if عد[ع] > عد[أفضل] or (عد[ع] == عد[أفضل] and ع < أفضل):
      # apl-source:25
      أفضل = ع
  # apl-source:26
  return أفضل
# apl-source:27

# apl-source:28
تأكد_يساوي(المنوال([1, 2, 2, 3]), 2, "واضح")
# apl-source:29
تأكد_يساوي(المنوال([4, 1, 4, 1]), 1, "تعادل")
# apl-source:30
تأكد_يساوي(المنوال([7]), 7, "وحيد")
# apl-source:31
