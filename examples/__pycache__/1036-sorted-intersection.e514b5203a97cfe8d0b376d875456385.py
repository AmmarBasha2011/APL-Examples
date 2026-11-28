
# apl-source:1
# مثال 1036 — تقاطع قائمتين مرتبتين
# apl-source:2
# Intersection of sorted arrays
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1036-sorted-intersection.apl
# apl-source:6

# apl-source:7
# نتقدم في القائمة ذات العنصر الأصغر
# apl-source:8
# وعند التساوي نسجل العنصر مرة واحدة
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
  ناتج = []
  # apl-source:20
  ي = 0
  # apl-source:21
  ك = 0
  # apl-source:22
  while (ي < len(أ)) and (ك < len(ب)):
    # apl-source:23
    if أ[ي] < ب[ك]:
      # apl-source:24
      ي = ي + 1
    # apl-source:25
    elif أ[ي] > ب[ك]:
      # apl-source:26
      ك = ك + 1
    # apl-source:27
    else:
      # apl-source:28
      if (len(ناتج) == 0) or (ناتج[len(ناتج) - 1] != أ[ي]):
        # apl-source:29
        ناتج = ناتج + [أ[ي]]
      # apl-source:30
      ي = ي + 1
      # apl-source:31
      ك = ك + 1
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
تأكد_يساوي(تقاطع([1, 2, 2, 3], [2, 2, 3, 4]), [2, 3], "مكرر")
# apl-source:35
تأكد_يساوي(تقاطع([1, 5], [2, 6]), [], "لا مشترك")
# apl-source:36
تأكد_يساوي(تقاطع([1, 2, 3], [1, 2, 3]), [1, 2, 3], "متطابقتان")
# apl-source:37
