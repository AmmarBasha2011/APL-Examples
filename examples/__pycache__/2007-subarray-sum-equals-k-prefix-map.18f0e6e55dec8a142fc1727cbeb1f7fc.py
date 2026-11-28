
# apl-source:1
# مثال 2007 — عدد المصفوفات الجزئية بمجموع ك
# apl-source:2
# Subarray sum equals k
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2007-subarray-sum-equals-k-prefix-map.apl
# apl-source:6

# apl-source:7
# # إن وجدنا بادئة تساوي المجموع الحالي ناقص ك
# apl-source:8
# # فكل تكرار منها يعطي مصفوفة جزئية
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
def عد(ق, ك):
  # apl-source:19
  رأينا = {}
  # apl-source:20
  رأينا[0] = 1
  # apl-source:21
  مج = 0
  # apl-source:22
  ناتج = 0
  # apl-source:23
  for ع in ق:
    # apl-source:24
    مج = مج + ع
    # apl-source:25
    ناتج = ناتج + رأينا.get(مج - ك, 0)
    # apl-source:26
    رأينا[مج] = رأينا.get(مج, 0) + 1
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(عد([1, 1, 1], 2), 2, "ثلاثة آحاد")
# apl-source:30
تأكد_يساوي(عد([1, 2, 3], 3), 2, "١٢٣")
# apl-source:31
تأكد_يساوي(عد([1, -1, 0], 0), 3, "مع سالب")
# apl-source:32
