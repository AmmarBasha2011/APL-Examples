
# apl-source:1
# مثال 1547 — الجداء الاتجاهي لمتجهين
# apl-source:2
# Cross product of two 3D vectors
# apl-source:3
# Demonstrates: هندسة ثلاثية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1547-cross-product-3d.apl
# apl-source:6

# apl-source:7
# المركبة الأولى من فرق ضربين
# apl-source:8
# نتبع الترتيب الدوري
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
def جداء_اتجاهي(أ, ب):
  # apl-source:19
  س = أ[1] * ب[2] - أ[2] * ب[1]
  # apl-source:20
  ص = أ[2] * ب[0] - أ[0] * ب[2]
  # apl-source:21
  ع = أ[0] * ب[1] - أ[1] * ب[0]
  # apl-source:22
  return [س, ص, ع]
# apl-source:23

# apl-source:24
تأكد_يساوي(جداء_اتجاهي([1, 0, 0], [0, 1, 0]), [0, 0, 1], "محورا س وص")
# apl-source:25
تأكد_يساوي(جداء_اتجاهي([1, 2, 3], [4, 5, 6]), [-3, 6, -3], "عادي")
# apl-source:26
تأكد_يساوي(جداء_اتجاهي([2, 2, 2], [1, 1, 1]), [0, 0, 0], "متوازيان")
# apl-source:27
