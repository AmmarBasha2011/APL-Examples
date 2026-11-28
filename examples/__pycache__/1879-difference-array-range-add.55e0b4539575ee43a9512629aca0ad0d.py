
# apl-source:1
# مثال 1879 — مصفوفة الفروق لإضافة مدى
# apl-source:2
# Range add with difference array
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1879-difference-array-range-add.apl
# apl-source:6

# apl-source:7
# نضيف عند البداية ونطرح بعد النهاية
# apl-source:8
# نجمع تراكمياً في النهاية
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
def طبّق(ن, عمليات):
  # apl-source:19
  فرق = []
  # apl-source:20
  for ك in range(ن + 1):
    # apl-source:21
    فرق.append(0)
  # apl-source:22
  for ع in عمليات:
    # apl-source:23
    فرق[ع[0]] = فرق[ع[0]] + ع[2]
    # apl-source:24
    فرق[ع[1] + 1] = فرق[ع[1] + 1] - ع[2]
  # apl-source:25
  ناتج = []
  # apl-source:26
  حالي = 0
  # apl-source:27
  for ك in range(ن):
    # apl-source:28
    حالي = حالي + فرق[ك]
    # apl-source:29
    ناتج.append(حالي)
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(طبّق(5, [[1, 3, 2], [2, 4, 3]]), [0, 2, 5, 5, 3], "عمليتان")
# apl-source:33
تأكد_يساوي(طبّق(3, []), [0, 0, 0], "لا عمليات")
# apl-source:34
تأكد_يساوي(طبّق(2, [[0, 1, 7]]), [7, 7], "كاملة")
# apl-source:35
