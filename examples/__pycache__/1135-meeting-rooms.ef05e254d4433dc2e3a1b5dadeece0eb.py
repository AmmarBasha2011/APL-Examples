
# apl-source:1
# مثال 1135 — قاعات اجتماعات
# apl-source:2
# Minimum meeting rooms
# apl-source:3
# Demonstrates: ترتيب الأحداث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1135-meeting-rooms.apl
# apl-source:6

# apl-source:7
# نفرز أوقات البدء وأوقات الانتهاء كلاً على حدة
# apl-source:8
# ونعدّ أقصى تداخل في أي لحظة
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
def قاعات(اجتماعات):
  # apl-source:19
  بدايات = []
  # apl-source:20
  نهايات = []
  # apl-source:21
  for ج in اجتماعات:
    # apl-source:22
    بدايات = بدايات + [ج[0]]
    # apl-source:23
    نهايات = نهايات + [ج[1]]
  # apl-source:24
  بدايات = sorted(بدايات)
  # apl-source:25
  نهايات = sorted(نهايات)
  # apl-source:26
  ن = 0
  # apl-source:27
  ك = 0
  # apl-source:28
  اقصى = 0
  # apl-source:29
  حالي = 0
  # apl-source:30
  while ن < len(بدايات):
    # apl-source:31
    if بدايات[ن] < نهايات[ك]:
      # apl-source:32
      حالي = حالي + 1
      # apl-source:33
      ن = ن + 1
      # apl-source:34
      if حالي > اقصى:
        # apl-source:35
        اقصى = حالي
    # apl-source:36
    else:
      # apl-source:37
      حالي = حالي - 1
      # apl-source:38
      ك = ك + 1
  # apl-source:39
  return اقصى
# apl-source:40

# apl-source:41
تأكد_يساوي(قاعات([[0,30],[5,10],[15,20]]), 2, "قاعتان")
# apl-source:42
تأكد_يساوي(قاعات([[7,10],[2,4]]), 1, "قاعة واحدة")
# apl-source:43
تأكد_يساوي(قاعات([[1,5],[2,6],[3,7],[4,8]]), 4, "أربع قاعات")
# apl-source:44
تأكد_يساوي(قاعات([[1,2],[2,3],[3,4]]), 1, "متتالية")
# apl-source:45
