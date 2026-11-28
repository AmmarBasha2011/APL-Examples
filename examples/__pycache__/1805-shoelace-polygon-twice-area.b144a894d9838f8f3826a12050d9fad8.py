
# apl-source:1
# مثال 1805 — ضعف مساحة المضلع بصيغة الحذاء
# apl-source:2
# Shoelace twice-area
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1805-shoelace-polygon-twice-area.apl
# apl-source:6

# apl-source:7
# نتجنب الكسور بضعف المساحة
# apl-source:8
# نأخذ القيمة المطلقة
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
def ضعف_المساحة(نقاط):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  ن = len(نقاط)
  # apl-source:21
  for ك in range(ن):
    # apl-source:22
    أ = نقاط[ك]
    # apl-source:23
    ب = نقاط[(ك + 1) % ن]
    # apl-source:24
    مجموع = مجموع + أ[0] * ب[1] - ب[0] * أ[1]
  # apl-source:25
  if مجموع < 0:
    # apl-source:26
    مجموع = -مجموع
  # apl-source:27
  return مجموع
# apl-source:28

# apl-source:29
تأكد_يساوي(ضعف_المساحة([[0, 0], [4, 0], [4, 3], [0, 3]]), 24, "مستطيل")
# apl-source:30
تأكد_يساوي(ضعف_المساحة([[0, 0], [4, 0], [0, 3]]), 12, "مثلث")
# apl-source:31
تأكد_يساوي(ضعف_المساحة([[0, 3], [4, 3], [4, 0], [0, 0]]), 24, "معكوس")
# apl-source:32
