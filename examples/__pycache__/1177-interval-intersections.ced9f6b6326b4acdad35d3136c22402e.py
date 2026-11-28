
# apl-source:1
# مثال 1177 — تقاطع المجالات
# apl-source:2
# Interval list intersections
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1177-interval-intersections.apl
# apl-source:6

# apl-source:7
# نقارن مجالين في كل خطوة
# apl-source:8
# ونتقدم في القائمة التي ينتهي مجالها أولاً
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
def تقاطعات(أ, ب):
  # apl-source:19
  ناتج = []
  # apl-source:20
  ي = 0
  # apl-source:21
  ك = 0
  # apl-source:22
  while (ي < len(أ)) and (ك < len(ب)):
    # apl-source:23
    بداية = max(أ[ي][0], ب[ك][0])
    # apl-source:24
    نهاية = min(أ[ي][1], ب[ك][1])
    # apl-source:25
    if بداية <= نهاية:
      # apl-source:26
      ناتج = ناتج + [[بداية, نهاية]]
    # apl-source:27
    if أ[ي][1] < ب[ك][1]:
      # apl-source:28
      ي = ي + 1
    # apl-source:29
    else:
      # apl-source:30
      ك = ك + 1
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
أ = [[0,2],[5,10],[13,23],[24,25]]
# apl-source:34
ب = [[1,5],[8,12],[15,24],[25,26]]
# apl-source:35
تأكد_يساوي(تقاطعات(أ, ب), [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]], "مثال أول")
# apl-source:36
تأكد_يساوي(تقاطعات([], [[1,3]]), [], "فارغة")
# apl-source:37
تأكد_يساوي(تقاطعات([[1,3]], [[4,5]]), [], "لا تقاطع")
# apl-source:38
