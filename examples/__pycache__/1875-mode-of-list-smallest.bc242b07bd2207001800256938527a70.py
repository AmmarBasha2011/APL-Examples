
# apl-source:1
# مثال 1875 — المنوال الأصغر
# apl-source:2
# Mode with smallest tie
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1875-mode-of-list-smallest.apl
# apl-source:6

# apl-source:7
# نعد التكرار بقاموس
# apl-source:8
# عند التعادل الأصغر قيمة
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
def منوال(ق):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ع in ق:
    # apl-source:21
    عد[str(ع)] = عد.get(str(ع), 0) + 1
  # apl-source:22
  أفضل = ق[0]
  # apl-source:23
  أعلى = 0
  # apl-source:24
  for ع in ق:
    # apl-source:25
    ج = عد[str(ع)]
    # apl-source:26
    if ج > أعلى or (ج == أعلى and ع < أفضل):
      # apl-source:27
      أعلى = ج
      # apl-source:28
      أفضل = ع
  # apl-source:29
  return أفضل
# apl-source:30

# apl-source:31
تأكد_يساوي(منوال([1, 2, 2, 3, 3]), 2, "تعادل")
# apl-source:32
تأكد_يساوي(منوال([5]), 5, "واحد")
# apl-source:33
تأكد_يساوي(منوال([4, 4, 1, 1, 1]), 1, "أغلبية")
# apl-source:34
