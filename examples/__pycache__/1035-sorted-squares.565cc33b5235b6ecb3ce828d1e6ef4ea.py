
# apl-source:1
# مثال 1035 — مربعات مرتبة
# apl-source:2
# Squares of a sorted array
# apl-source:3
# Demonstrates: مؤشران من الطرفين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1035-sorted-squares.apl
# apl-source:6

# apl-source:7
# أكبر مربع عند أحد الطرفين لأن السالب الكبير مربعه كبير
# apl-source:8
# نملأ الناتج من النهاية بالأكبر
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
def مربعات(ق):
  # apl-source:19
  ن = len(ق)
  # apl-source:20
  ناتج = [0] * ن
  # apl-source:21
  ي = 0
  # apl-source:22
  ل = ن - 1
  # apl-source:23
  for ع in range(ن - 1, -1, -1):
    # apl-source:24
    if (ق[ي] * ق[ي]) > (ق[ل] * ق[ل]):
      # apl-source:25
      ناتج[ع] = ق[ي] * ق[ي]
      # apl-source:26
      ي = ي + 1
    # apl-source:27
    else:
      # apl-source:28
      ناتج[ع] = ق[ل] * ق[ل]
      # apl-source:29
      ل = ل - 1
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(مربعات([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100], "مختلطة")
# apl-source:33
تأكد_يساوي(مربعات([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121], "تكرار")
# apl-source:34
تأكد_يساوي(مربعات([1, 2, 3]), [1, 4, 9], "موجبة")
# apl-source:35
