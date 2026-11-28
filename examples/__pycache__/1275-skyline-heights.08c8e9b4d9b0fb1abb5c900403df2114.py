
# apl-source:1
# مثال 1275 — أفق المدينة
# apl-source:2
# Building skyline outline
# apl-source:3
# Demonstrates: مسح بأحداث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1275-skyline-heights.apl
# apl-source:6

# apl-source:7
# نمسح الأحداث بالترتيب ونحتفظ بأعلى مبنى نشط
# apl-source:8
# وكل تغير في الأعلى نقطة في الأفق
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
def افق(مباني):
  # apl-source:19
  احداث = []
  # apl-source:20
  for م in مباني:
    # apl-source:21
    احداث = احداث + [[م[0], -م[2]]]
    # apl-source:22
    احداث = احداث + [[م[1], م[2]]]
  # apl-source:23
  احداث = sorted(احداث)
  # apl-source:24
  نشطة = [0]
  # apl-source:25
  سابق = 0
  # apl-source:26
  ناتج = []
  # apl-source:27
  for ح in احداث:
    # apl-source:28
    if ح[1] < 0:
      # apl-source:29
      نشطة = نشطة + [-ح[1]]
    # apl-source:30
    else:
      # apl-source:31
      نشطة.remove(ح[1])
    # apl-source:32
    اعلى = 0
    # apl-source:33
    for ق in نشطة:
      # apl-source:34
      if ق > اعلى:
        # apl-source:35
        اعلى = ق
    # apl-source:36
    if اعلى != سابق:
      # apl-source:37
      ناتج = ناتج + [[ح[0], اعلى]]
      # apl-source:38
      سابق = اعلى
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
تأكد_يساوي(افق([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]), [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]], "مثال أول")
# apl-source:42
تأكد_يساوي(افق([[0,2,3],[2,5,3]]), [[0,3],[5,0]], "متلاصقان")
# apl-source:43
