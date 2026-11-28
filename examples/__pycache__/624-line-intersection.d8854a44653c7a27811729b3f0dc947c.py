
# apl-source:1
# مثال 624 — تقاطع القطع المستقيمة
# apl-source:2
# Segment intersection
# apl-source:3
# Demonstrates: اتجاه، تقاطع، هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/624-line-intersection.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# تقاطع القطع المستقيمة باختبارات الاتجاه
# apl-source:25
# Demonstrates: جداء اتجاهي, فحص تداخل, حالات عامة
# apl-source:26
# أساس الرسوميات وأنظمة المعلومات الجغرافية
# apl-source:27

# apl-source:28
def اتجاه(ن1, ن2, ن3):
  # apl-source:29
  return (ن2[0] - ن1[0]) * (ن3[1] - ن1[1]) - (ن2[1] - ن1[1]) * (ن3[0] - ن1[0])
# apl-source:30

# apl-source:31
def يتقاطعان(أ1, أ2, ب1, ب2):
  # apl-source:32
  ج1 = اتجاه(أ1, أ2, ب1)
  # apl-source:33
  ج2 = اتجاه(أ1, أ2, ب2)
  # apl-source:34
  ج3 = اتجاه(ب1, ب2, أ1)
  # apl-source:35
  ج4 = اتجاه(ب1, ب2, أ2)
  # apl-source:36
  return (ج1 > 0 and ج2 < 0 or ج1 < 0 and ج2 > 0) and (ج3 > 0 and ج4 < 0 or ج3 < 0 and ج4 > 0)
# apl-source:37

# apl-source:38
تأكد_يساوي(يتقاطعان([0,0],[4,4],[0,4],[4,0]), True, "قطرا مربع")
# apl-source:39
تأكد_يساوي(يتقاطعان([0,0],[1,1],[0,2],[2,3]), False, "متوازيان بعيدان")
# apl-source:40
تأكد_يساوي(يتقاطعان([0,0],[4,0],[2,-1],[2,1]), True, "عمودي على أفقي")
# apl-source:41
print("قطران يتقاطعان:", يتقاطعان([0,0],[4,4],[0,4],[4,0]))
# apl-source:42
