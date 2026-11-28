
# apl-source:1
# مثال 1546 — الجداء النقطي لمتجهين
# apl-source:2
# Dot product of two 3D vectors
# apl-source:3
# Demonstrates: هندسة ثلاثية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1546-dot-product-3d.apl
# apl-source:6

# apl-source:7
# نضرب المركبات الثلاث
# apl-source:8
# الصفر يعني أن المتجهين متعامدان
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
def جداء_نقطي(أ, ب):
  # apl-source:19
  return أ[0] * ب[0] + أ[1] * ب[1] + أ[2] * ب[2]
# apl-source:20

# apl-source:21
تأكد_يساوي(جداء_نقطي([1, 2, 3], [4, 5, 6]), 32, "عادي")
# apl-source:22
تأكد_يساوي(جداء_نقطي([1, 0, 0], [0, 1, 0]), 0, "متعامدان")
# apl-source:23
تأكد_يساوي(جداء_نقطي([2, 2, 2], [-1, -1, -1]), -6, "متعاكسان")
# apl-source:24
