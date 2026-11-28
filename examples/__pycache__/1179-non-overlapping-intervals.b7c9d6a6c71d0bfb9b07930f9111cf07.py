
# apl-source:1
# مثال 1179 — مجالات غير متداخلة
# apl-source:2
# Minimum removals for non overlapping intervals
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1179-non-overlapping-intervals.apl
# apl-source:6

# apl-source:7
# نرتب بحسب النهاية
# apl-source:8
# ونحذف أي مجال يبدأ قبل نهاية آخر مجال مقبول
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
def اقل_حذف(مجالات):
  # apl-source:19
  if len(مجالات) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  ازواج = []
  # apl-source:22
  for م in مجالات:
    # apl-source:23
    ازواج = ازواج + [[م[1], م[0]]]
  # apl-source:24
  ازواج = sorted(ازواج)
  # apl-source:25
  نهاية = ازواج[0][0]
  # apl-source:26
  حذف_ = 0
  # apl-source:27
  for ع in range(1, len(ازواج)):
    # apl-source:28
    if ازواج[ع][1] < نهاية:
      # apl-source:29
      حذف_ = حذف_ + 1
    # apl-source:30
    else:
      # apl-source:31
      نهاية = ازواج[ع][0]
  # apl-source:32
  return حذف_
# apl-source:33

# apl-source:34
تأكد_يساوي(اقل_حذف([[1,2],[2,3],[3,4],[1,3]]), 1, "مثال أول")
# apl-source:35
تأكد_يساوي(اقل_حذف([[1,2],[1,2],[1,2]]), 2, "متطابقة")
# apl-source:36
تأكد_يساوي(اقل_حذف([[1,2],[2,3]]), 0, "لا حذف")
# apl-source:37
تأكد_يساوي(اقل_حذف([]), 0, "فارغة")
# apl-source:38
