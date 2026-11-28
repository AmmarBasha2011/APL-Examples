
# apl-source:1
# مثال 1635 — أقرب ك عنصراً في قائمة مرتبة
# apl-source:2
# K closest elements in sorted list
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1635-k-closest-elements-sorted.apl
# apl-source:6

# apl-source:7
# نضيّق النافذة من الطرفين
# apl-source:8
# نحذف الأبعد عن الهدف
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
def أقرب_ك(أ, ك, س):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = len(أ) - 1
  # apl-source:21
  while ج - ي + 1 > ك:
    # apl-source:22
    فرق_ي = س - أ[ي]
    # apl-source:23
    فرق_ج = أ[ج] - س
    # apl-source:24
    if فرق_ي < 0:
      # apl-source:25
      فرق_ي = -فرق_ي
    # apl-source:26
    if فرق_ج < 0:
      # apl-source:27
      فرق_ج = -فرق_ج
    # apl-source:28
    if فرق_ي > فرق_ج:
      # apl-source:29
      ي = ي + 1
    # apl-source:30
    else:
      # apl-source:31
      ج = ج - 1
  # apl-source:32
  return أ[ي:ج + 1]
# apl-source:33

# apl-source:34
تأكد_يساوي(أقرب_ك([1, 2, 3, 4, 5], 4, 3), [1, 2, 3, 4], "وسط")
# apl-source:35
تأكد_يساوي(أقرب_ك([1, 2, 3, 4, 5], 4, -1), [1, 2, 3, 4], "قبل")
# apl-source:36
تأكد_يساوي(أقرب_ك([1, 5, 9], 1, 6), [5], "واحد")
# apl-source:37
