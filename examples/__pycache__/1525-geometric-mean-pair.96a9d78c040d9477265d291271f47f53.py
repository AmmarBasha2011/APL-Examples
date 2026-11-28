
# apl-source:1
# مثال 1525 — المتوسط الهندسي
# apl-source:2
# Geometric mean
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1525-geometric-mean-pair.apl
# apl-source:6

# apl-source:7
# نضرب القيم
# apl-source:8
# نأخذ الجذر بعدد القيم
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
def متوسط_هندسي(أ):
  # apl-source:19
  حاصل = 1
  # apl-source:20
  for ع in أ:
    # apl-source:21
    حاصل = حاصل * ع
  # apl-source:22
  return حاصل ** (1 / len(أ))
# apl-source:23

# apl-source:24
تأكد_يساوي(متوسط_هندسي([2, 8]), 4.0, "اثنان")
# apl-source:25
تأكد_يساوي(متوسط_هندسي([5, 5]), 5.0, "متساويان")
# apl-source:26
تأكد_يساوي(متوسط_هندسي([9]), 9.0, "قيمة واحدة")
# apl-source:27
