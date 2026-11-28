
# apl-source:1
# مثال 1447 — نقاط شبكية على قطعة
# apl-source:2
# Lattice points on a segment
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1447-lattice-points-on-segment.apl
# apl-source:6

# apl-source:7
# العدد يساوي القاسم المشترك الأكبر للفرقين زائد واحد
# apl-source:8
# الطرفان محسوبان
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
def قاسم(أ, ب):
  # apl-source:19
  if أ < 0:
    # apl-source:20
    أ = -أ
  # apl-source:21
  if ب < 0:
    # apl-source:22
    ب = -ب
  # apl-source:23
  while ب != 0:
    # apl-source:24
    ت = أ % ب
    # apl-source:25
    أ = ب
    # apl-source:26
    ب = ت
  # apl-source:27
  return أ
# apl-source:28

# apl-source:29
def نقاط_القطعة(أ, ب):
  # apl-source:30
  return قاسم(ب[0] - أ[0], ب[1] - أ[1]) + 1
# apl-source:31

# apl-source:32
تأكد_يساوي(نقاط_القطعة([0,0], [4,2]), 3, "ثلاث")
# apl-source:33
تأكد_يساوي(نقاط_القطعة([0,0], [5,0]), 6, "أفقية")
# apl-source:34
تأكد_يساوي(نقاط_القطعة([1,1], [1,1]), 1, "نقطة")
# apl-source:35
