
# apl-source:1
# مثال 1310 — مجموعات جزئية مميزة
# apl-source:2
# Subsets with duplicates
# apl-source:3
# Demonstrates: رجوع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1310-subsets-unique.apl
# apl-source:6

# apl-source:7
# نرتب القائمة ونضيف كل عنصر لما قبله
# apl-source:8
# ونتجنب المجموعات المكررة
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
def مجموعات(أ):
  # apl-source:19
  ناتج = [[]]
  # apl-source:20
  for س in sorted(أ):
    # apl-source:21
    جديد = []
    # apl-source:22
    for ق in ناتج:
      # apl-source:23
      ن = ق + [س]
      # apl-source:24
      if ن not in ناتج:
        # apl-source:25
        جديد = جديد + [ن]
    # apl-source:26
    ناتج = ناتج + جديد
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(len(مجموعات([1,2,2])), 6, "ست")
# apl-source:30
تأكد_يساوي(مجموعات([0]), [[], [0]], "صفر")
# apl-source:31
تأكد_يساوي(len(مجموعات([1,1,1])), 4, "أربع")
# apl-source:32
تأكد_يساوي(مجموعات([]), [[]], "فارغة")
# apl-source:33
