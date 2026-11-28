
# apl-source:1
# مثال 1548 — طول متجه ثلاثي
# apl-source:2
# Length of a 3D vector
# apl-source:3
# Demonstrates: هندسة ثلاثية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1548-vector-length-3d.apl
# apl-source:6

# apl-source:7
# نربع كل مركبة
# apl-source:8
# نجمع ونأخذ الجذر
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
def طول_المتجه(أ):
  # apl-source:19
  return (أ[0] ** 2 + أ[1] ** 2 + أ[2] ** 2) ** 0.5
# apl-source:20

# apl-source:21
تأكد_يساوي(طول_المتجه([3, 4, 0]), 5.0, "ثلاثة وأربعة")
# apl-source:22
تأكد_يساوي(طول_المتجه([2, 3, 6]), 7.0, "سبعة")
# apl-source:23
تأكد_يساوي(طول_المتجه([0, 0, 0]), 0.0, "صفر")
# apl-source:24
