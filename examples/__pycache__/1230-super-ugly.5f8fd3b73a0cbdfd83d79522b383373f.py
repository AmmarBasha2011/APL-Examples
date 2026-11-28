
# apl-source:1
# مثال 1230 — عدد قبيح فائق
# apl-source:2
# Super ugly number
# apl-source:3
# Demonstrates: مؤشرات متعددة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1230-super-ugly.apl
# apl-source:6

# apl-source:7
# لكل أولي مؤشر في القائمة المبنية
# apl-source:8
# نأخذ الأصغر ونحرك كل المؤشرات التي أنتجته
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
def قبيح_فائق(ن, اوليات):
  # apl-source:19
  أ = [1]
  # apl-source:20
  مؤشرات = [0] * len(اوليات)
  # apl-source:21
  while len(أ) < ن:
    # apl-source:22
    مرشحون = []
    # apl-source:23
    for ع in range(len(اوليات)):
      # apl-source:24
      مرشحون = مرشحون + [أ[مؤشرات[ع]] * اوليات[ع]]
    # apl-source:25
    ت = مرشحون[0]
    # apl-source:26
    for م in مرشحون:
      # apl-source:27
      if م < ت:
        # apl-source:28
        ت = م
    # apl-source:29
    أ = أ + [ت]
    # apl-source:30
    for ع in range(len(اوليات)):
      # apl-source:31
      if مرشحون[ع] == ت:
        # apl-source:32
        مؤشرات[ع] = مؤشرات[ع] + 1
  # apl-source:33
  return أ[ن - 1]
# apl-source:34

# apl-source:35
تأكد_يساوي(قبيح_فائق(12, [2,7,13,19]), 32, "مثال أول")
# apl-source:36
تأكد_يساوي(قبيح_فائق(1, [2,3,5]), 1, "الأول")
# apl-source:37
تأكد_يساوي(قبيح_فائق(10, [2,3,5]), 12, "مثل القبيح")
# apl-source:38
