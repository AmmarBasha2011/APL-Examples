
# apl-source:1
# مثال 623 — نقطة داخل مضلع
# apl-source:2
# Point in polygon
# apl-source:3
# Demonstrates: شعاع، تكافؤ، مضلع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/623-point-in-polygon.apl
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
# نقطة داخل مضلع؟ قذف شعاع أفقي
# apl-source:25
# Demonstrates: تقاطع شعاع مع أضلاع, تكافؤ عدد التقاطعات
# apl-source:26
# عدد فردي من التقاطعات يعني أن النقطة بالداخل
# apl-source:27

# apl-source:28
def داخل(نقطة, مضلع):
  # apl-source:29
  س = نقطة[0]
  # apl-source:30
  ص = نقطة[1]
  # apl-source:31
  تقاطعات = 0
  # apl-source:32
  ن = len(مضلع)
  # apl-source:33
  for ي in range(ن):
    # apl-source:34
    أ = مضلع[ي]
    # apl-source:35
    ب = مضلع[(ي + 1) % ن]
    # apl-source:36
    if (أ[1] > ص) != (ب[1] > ص):
      # apl-source:37
      س_تقاطع = أ[0] + (ص - أ[1]) * (ب[0] - أ[0]) / (ب[1] - أ[1])
      # apl-source:38
      if س < س_تقاطع:
        # apl-source:39
        تقاطعات = تقاطعات + 1
  # apl-source:40
  return تقاطعات % 2 == 1
# apl-source:41

# apl-source:42
مربع = [[0, 0], [10, 0], [10, 10], [0, 10]]
# apl-source:43
تأكد_يساوي(داخل([5, 5], مربع), True, "المنتصف داخل")
# apl-source:44
تأكد_يساوي(داخل([15, 5], مربع), False, "خارج يمينا")
# apl-source:45
تأكد_يساوي(داخل([5, 15], مربع), False, "خارج أعلى")
# apl-source:46
مثلث = [[0, 0], [10, 0], [5, 10]]
# apl-source:47
تأكد_يساوي(داخل([5, 3], مثلث), True, "داخل مثلث")
# apl-source:48
تأكد_يساوي(داخل([1, 9], مثلث), False, "خارج مثلث")
# apl-source:49
print("اختبار (5,5) في مربع:", داخل([5, 5], مربع))
# apl-source:50
