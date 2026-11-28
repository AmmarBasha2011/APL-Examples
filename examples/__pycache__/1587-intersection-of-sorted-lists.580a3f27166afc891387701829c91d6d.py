
# apl-source:1
# مثال 1587 — تقاطع قائمتين مرتبتين
# apl-source:2
# Intersection of sorted lists
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1587-intersection-of-sorted-lists.apl
# apl-source:6

# apl-source:7
# مؤشر لكل قائمة
# apl-source:8
# نقدم الأصغر ونسجل عند التساوي
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
def تقاطع(أ, ب):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = 0
  # apl-source:21
  ناتج = []
  # apl-source:22
  while ي < len(أ) and ج < len(ب):
    # apl-source:23
    if أ[ي] == ب[ج]:
      # apl-source:24
      ناتج.append(أ[ي])
      # apl-source:25
      ي = ي + 1
      # apl-source:26
      ج = ج + 1
    # apl-source:27
    elif أ[ي] < ب[ج]:
      # apl-source:28
      ي = ي + 1
    # apl-source:29
    else:
      # apl-source:30
      ج = ج + 1
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
تأكد_يساوي(تقاطع([1, 2, 4, 5], [2, 3, 5, 7]), [2, 5], "مشتركان")
# apl-source:34
تأكد_يساوي(تقاطع([1, 2], [3, 4]), [], "بلا تقاطع")
# apl-source:35
تأكد_يساوي(تقاطع([], [1]), [], "فارغة")
# apl-source:36
