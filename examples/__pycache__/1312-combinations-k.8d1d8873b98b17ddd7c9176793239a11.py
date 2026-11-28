
# apl-source:1
# مثال 1312 — تركيبات k
# apl-source:2
# Combinations n choose k
# apl-source:3
# Demonstrates: بناء تراكمي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1312-combinations-k.apl
# apl-source:6

# apl-source:7
# نبني الاختيارات بترتيب تصاعدي
# apl-source:8
# فلا يتكرر اختيار بترتيب مختلف
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
def تركيبات_ك(ن, ك):
  # apl-source:19
  ناتج = [[]]
  # apl-source:20
  for ر in range(ك):
    # apl-source:21
    جديد = []
    # apl-source:22
    for ق in ناتج:
      # apl-source:23
      بداية = 1
      # apl-source:24
      if len(ق) > 0:
        # apl-source:25
        بداية = ق[-1] + 1
      # apl-source:26
      for س in range(بداية, ن + 1):
        # apl-source:27
        جديد = جديد + [ق + [س]]
    # apl-source:28
    ناتج = جديد
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(تركيبات_ك(4, 2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]], "أربعة واثنان")
# apl-source:32
تأكد_يساوي(تركيبات_ك(1, 1), [[1]], "واحد")
# apl-source:33
تأكد_يساوي(len(تركيبات_ك(6, 3)), 20, "ستة وثلاثة")
# apl-source:34
تأكد_يساوي(تركيبات_ك(3, 0), [[]], "صفر")
# apl-source:35
