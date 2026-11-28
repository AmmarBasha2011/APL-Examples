
# apl-source:1
# مثال 1321 — منقول مصفوفة
# apl-source:2
# Transpose rectangular matrix
# apl-source:3
# Demonstrates: شبكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1321-transpose-matrix.apl
# apl-source:6

# apl-source:7
# الصف i والعمود j يصبحان الصف j والعمود i
# apl-source:8
# الناتج أبعاده معكوسة
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
def انقل(م):
  # apl-source:19
  if len(م) == 0:
    # apl-source:20
    return []
  # apl-source:21
  ناتج = []
  # apl-source:22
  for ج in range(len(م[0])):
    # apl-source:23
    صف = []
    # apl-source:24
    for ص in range(len(م)):
      # apl-source:25
      صف = صف + [م[ص][ج]]
    # apl-source:26
    ناتج = ناتج + [صف]
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(انقل([[1,2,3],[4,5,6]]), [[1,4],[2,5],[3,6]], "اثنان في ثلاثة")
# apl-source:30
تأكد_يساوي(انقل([[1,2],[3,4]]), [[1,3],[2,4]], "مربعة")
# apl-source:31
تأكد_يساوي(انقل(انقل([[1,2,3],[4,5,6]])), [[1,2,3],[4,5,6]], "مرتان")
# apl-source:32
تأكد_يساوي(انقل([]), [], "فارغة")
# apl-source:33
