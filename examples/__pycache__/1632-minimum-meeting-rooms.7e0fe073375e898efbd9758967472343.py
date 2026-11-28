
# apl-source:1
# مثال 1632 — أقل عدد غرف اجتماعات
# apl-source:2
# Minimum meeting rooms
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1632-minimum-meeting-rooms.apl
# apl-source:6

# apl-source:7
# نفرز البدايات والنهايات منفصلة
# apl-source:8
# نتتبع عدد الاجتماعات الجارية
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
def أقل_غرف(اجتماعات):
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
  جارية = 0
  # apl-source:27
  أقصى = 0
  # apl-source:28
  ج = 0
  # apl-source:29
  for ب in بدايات:
    # apl-source:30
    while نهايات[ج] <= ب:
      # apl-source:31
      جارية = جارية - 1
      # apl-source:32
      ج = ج + 1
    # apl-source:33
    جارية = جارية + 1
    # apl-source:34
    if جارية > أقصى:
      # apl-source:35
      أقصى = جارية
  # apl-source:36
  return أقصى
# apl-source:37

# apl-source:38
تأكد_يساوي(أقل_غرف([[0, 30], [5, 10], [15, 20]]), 2, "غرفتان")
# apl-source:39
تأكد_يساوي(أقل_غرف([[7, 10], [2, 4]]), 1, "غرفة واحدة")
# apl-source:40
تأكد_يساوي(أقل_غرف([[1, 5], [2, 6], [3, 7]]), 3, "ثلاث")
# apl-source:41
