
# apl-source:1
# مثال 2072 — فيبوناتشي بقوة مصفوفة 2×2
# apl-source:2
# Fibonacci by matrix power
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2072-fibonacci-by-2x2-matrix-power.apl
# apl-source:6

# apl-source:7
# # القوة ن تعطي F(n) في الخانة العلوية اليمنى
# apl-source:8
# # نربع المصفوفة بدل التكرار الخطي
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
def اضرب(ا, ب):
  # apl-source:19
  return [[ا[0][0] * ب[0][0] + ا[0][1] * ب[1][0], ا[0][0] * ب[0][1] + ا[0][1] * ب[1][1]], [ا[1][0] * ب[0][0] + ا[1][1] * ب[1][0], ا[1][0] * ب[0][1] + ا[1][1] * ب[1][1]]]
# apl-source:20

# apl-source:21
def فيب(ن):
  # apl-source:22
  ناتج = [[1, 0], [0, 1]]
  # apl-source:23
  اساس = [[1, 1], [1, 0]]
  # apl-source:24
  while ن > 0:
    # apl-source:25
    if ن % 2 == 1:
      # apl-source:26
      ناتج = اضرب(ناتج, اساس)
    # apl-source:27
    اساس = اضرب(اساس, اساس)
    # apl-source:28
    ن = ن // 2
  # apl-source:29
  return ناتج[0][1]
# apl-source:30

# apl-source:31
تأكد_يساوي(فيب(0), 0, "صفر")
# apl-source:32
تأكد_يساوي(فيب(1), 1, "واحد")
# apl-source:33
تأكد_يساوي(فيب(10), 55, "عشرة")
# apl-source:34
تأكد_يساوي(فيب(50), 12586269025, "خمسون")
# apl-source:35
