
# apl-source:1
# مثال 1738 — عدد قاعات الاجتماعات
# apl-source:2
# Minimum meeting rooms needed
# apl-source:3
# Demonstrates: فترات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1738-meeting-rooms-needed-count.apl
# apl-source:6

# apl-source:7
# نفرز البدايات والنهايات
# apl-source:8
# نتتبع العدد الحالي
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
  for ا in اجتماعات:
    # apl-source:22
    بدايات.append(ا[0])
    # apl-source:23
    نهايات.append(ا[1])
  # apl-source:24
  بدايات.sort()
  # apl-source:25
  نهايات.sort()
  # apl-source:26
  ي = 0
  # apl-source:27
  ك = 0
  # apl-source:28
  حالي = 0
  # apl-source:29
  أعلى = 0
  # apl-source:30
  while ي < len(بدايات):
    # apl-source:31
    if بدايات[ي] < نهايات[ك]:
      # apl-source:32
      حالي = حالي + 1
      # apl-source:33
      ي = ي + 1
      # apl-source:34
      أعلى = max(أعلى, حالي)
    # apl-source:35
    else:
      # apl-source:36
      حالي = حالي - 1
      # apl-source:37
      ك = ك + 1
  # apl-source:38
  return أعلى
# apl-source:39

# apl-source:40
تأكد_يساوي(قاعات([[0, 30], [5, 10], [15, 20]]), 2, "اثنتان")
# apl-source:41
تأكد_يساوي(قاعات([[1, 2], [3, 4]]), 1, "واحدة")
# apl-source:42
تأكد_يساوي(قاعات([[1, 5], [2, 6], [3, 7]]), 3, "ثلاث")
# apl-source:43
