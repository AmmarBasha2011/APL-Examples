
# apl-source:1
# مثال 1432 — تداخل مستطيلين
# apl-source:2
# Do two rectangles overlap
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1432-rectangle-overlap.apl
# apl-source:6

# apl-source:7
# التداخل يحتاج تقاطعاً في المحورين معاً
# apl-source:8
# اللمس عند الحافة لا يكفي
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
def يتداخلان(أ, ب):
  # apl-source:19
  افقي = (min(أ[2], ب[2]) - max(أ[0], ب[0])) > 0
  # apl-source:20
  رأسي = (min(أ[3], ب[3]) - max(أ[1], ب[1])) > 0
  # apl-source:21
  return افقي and رأسي
# apl-source:22

# apl-source:23
تأكد_يساوي(يتداخلان([0,0,2,2], [1,1,3,3]), True, "تداخل")
# apl-source:24
تأكد_يساوي(يتداخلان([0,0,1,1], [1,0,2,1]), False, "لمس")
# apl-source:25
تأكد_يساوي(يتداخلان([0,0,1,1], [2,2,3,3]), False, "منفصلان")
# apl-source:26
