
# apl-source:1
# مثال 1311 — مجموع التركيبات ٢
# apl-source:2
# Combination sum II no reuse
# apl-source:3
# Demonstrates: رجوع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1311-combination-sum-two.apl
# apl-source:6

# apl-source:7
# نرتب القائمة ونتخطى القيم المكررة في نفس المستوى
# apl-source:8
# وكل عنصر يستعمل مرة
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
def تركيبات(أ, هدف):
  # apl-source:19
  ق = sorted(أ)
  # apl-source:20
  ناتج = []
  # apl-source:21
  مكدس = [[0, [], 0]]
  # apl-source:22
  while len(مكدس) > 0:
    # apl-source:23
    ح = مكدس.pop()
    # apl-source:24
    بداية = ح[0]
    # apl-source:25
    مسار = ح[1]
    # apl-source:26
    مج = ح[2]
    # apl-source:27
    if مج == هدف:
      # apl-source:28
      if مسار not in ناتج:
        # apl-source:29
        ناتج = ناتج + [مسار]
    # apl-source:30
    if مج < هدف:
      # apl-source:31
      for ع in range(بداية, len(ق)):
        # apl-source:32
        if مج + ق[ع] <= هدف:
          # apl-source:33
          مكدس = مكدس + [[ع + 1, مسار + [ق[ع]], مج + ق[ع]]]
  # apl-source:34
  return sorted(ناتج)
# apl-source:35

# apl-source:36
تأكد_يساوي(تركيبات([10,1,2,7,6,1,5], 8), [[1,1,6],[1,2,5],[1,7],[2,6]], "مثال أول")
# apl-source:37
تأكد_يساوي(تركيبات([2,5,2,1,2], 5), [[1,2,2],[5]], "مثال ثان")
# apl-source:38
تأكد_يساوي(تركيبات([3], 5), [], "لا حل")
# apl-source:39
