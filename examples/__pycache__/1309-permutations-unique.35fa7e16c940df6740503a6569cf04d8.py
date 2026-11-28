
# apl-source:1
# مثال 1309 — تباديل بلا تكرار
# apl-source:2
# Permutations with duplicates
# apl-source:3
# Demonstrates: بناء تراكمي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1309-permutations-unique.apl
# apl-source:6

# apl-source:7
# ندرج العنصر الجديد في كل موضع
# apl-source:8
# ونحذف النتائج المكررة بالمقارنة
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
def تباديل(أ):
  # apl-source:19
  ناتج = [[]]
  # apl-source:20
  for س in أ:
    # apl-source:21
    جديد = []
    # apl-source:22
    for ق in ناتج:
      # apl-source:23
      for ع in range(len(ق) + 1):
        # apl-source:24
        ن = ق[:ع] + [س] + ق[ع:]
        # apl-source:25
        if ن not in جديد:
          # apl-source:26
          جديد = جديد + [ن]
    # apl-source:27
    ناتج = جديد
  # apl-source:28
  return sorted(ناتج)
# apl-source:29

# apl-source:30
تأكد_يساوي(تباديل([1,1,2]), [[1,1,2],[1,2,1],[2,1,1]], "مع تكرار")
# apl-source:31
تأكد_يساوي(len(تباديل([1,2,3])), 6, "ستة")
# apl-source:32
تأكد_يساوي(تباديل([]), [[]], "فارغة")
# apl-source:33
تأكد_يساوي(تباديل([5,5]), [[5,5]], "متطابقان")
# apl-source:34
