
# apl-source:1
# مثال 1274 — نطاقات متداخلة
# apl-source:2
# Count overlapping ranges by sweep
# apl-source:3
# Demonstrates: مسح خطي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1274-range-addition-sorted.apl
# apl-source:6

# apl-source:7
# نحول كل مجال إلى حدثي بداية ونهاية
# apl-source:8
# ونمسح بالترتيب لنعرف أقصى تداخل
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
def اقصى_تداخل(مجالات):
  # apl-source:19
  احداث = []
  # apl-source:20
  for م in مجالات:
    # apl-source:21
    احداث = احداث + [[م[0], 1]]
    # apl-source:22
    احداث = احداث + [[م[1] + 1, -1]]
  # apl-source:23
  احداث = sorted(احداث)
  # apl-source:24
  حالي = 0
  # apl-source:25
  اقصى = 0
  # apl-source:26
  for ح in احداث:
    # apl-source:27
    حالي = حالي + ح[1]
    # apl-source:28
    if حالي > اقصى:
      # apl-source:29
      اقصى = حالي
  # apl-source:30
  return اقصى
# apl-source:31

# apl-source:32
تأكد_يساوي(اقصى_تداخل([[1,5],[2,6],[4,8]]), 3, "ثلاثة")
# apl-source:33
تأكد_يساوي(اقصى_تداخل([[1,2],[3,4]]), 1, "منفصلة")
# apl-source:34
تأكد_يساوي(اقصى_تداخل([[1,3],[3,5]]), 2, "تلامس")
# apl-source:35
تأكد_يساوي(اقصى_تداخل([]), 0, "فارغة")
# apl-source:36
