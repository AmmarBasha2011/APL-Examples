
# apl-source:1
# مثال 1677 — الجداء النقطي لمتجهين
# apl-source:2
# Dot product of two vectors
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1677-dot-product-of-vectors.apl
# apl-source:6

# apl-source:7
# نضرب كل مركبتين متقابلتين
# apl-source:8
# نجمع الناتج
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
  مجموع = 0
  # apl-source:20
  for ك in range(len(أ)):
    # apl-source:21
    مجموع = مجموع + أ[ك] * ب[ك]
  # apl-source:22
  return مجموع
# apl-source:23

# apl-source:24
تأكد_يساوي(جداء_نقطي([1, 2, 3], [4, 5, 6]), 32, "ثلاثي")
# apl-source:25
تأكد_يساوي(جداء_نقطي([1, 0], [0, 1]), 0, "متعامدان")
# apl-source:26
تأكد_يساوي(جداء_نقطي([2], [5]), 10, "بعد واحد")
# apl-source:27
