
# apl-source:1
# مثال 1440 — فحص المضلع المحدب
# apl-source:2
# Convex polygon check
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1440-convex-polygon-check.apl
# apl-source:6

# apl-source:7
# ندور على الرؤوس ونحسب الجداء التقاطعي
# apl-source:8
# كل الإشارات يجب أن تتفق
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
def محدب(ن):
  # apl-source:19
  عدد = len(ن)
  # apl-source:20
  موجب = False
  # apl-source:21
  سالب = False
  # apl-source:22
  for ع in range(عدد):
    # apl-source:23
    أ = ن[ع]
    # apl-source:24
    ب = ن[(ع + 1) % عدد]
    # apl-source:25
    ج = ن[(ع + 2) % عدد]
    # apl-source:26
    ض = (ب[0] - أ[0]) * (ج[1] - ب[1]) - (ب[1] - أ[1]) * (ج[0] - ب[0])
    # apl-source:27
    if ض > 0:
      # apl-source:28
      موجب = True
    # apl-source:29
    if ض < 0:
      # apl-source:30
      سالب = True
  # apl-source:31
  مختلط = موجب and سالب
  # apl-source:32
  return مختلط == False
# apl-source:33

# apl-source:34
تأكد_يساوي(محدب([[0,0],[0,5],[5,5],[5,0]]), True, "مربع")
# apl-source:35
تأكد_يساوي(محدب([[0,0],[0,10],[10,10],[10,0],[5,5]]), False, "مقعر")
# apl-source:36
تأكد_يساوي(محدب([[0,0],[4,0],[0,3]]), True, "مثلث")
# apl-source:37
