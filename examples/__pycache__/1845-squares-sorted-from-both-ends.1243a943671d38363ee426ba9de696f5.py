
# apl-source:1
# مثال 1845 — مربعات مرتبة بمؤشرين
# apl-source:2
# Sorted squares with two pointers
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1845-squares-sorted-from-both-ends.apl
# apl-source:6

# apl-source:7
# الأكبر مربعاً عند أحد الطرفين
# apl-source:8
# نملأ النتيجة من النهاية
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
def مربعات_مرتبة(ق):
  # apl-source:19
  ن = len(ق)
  # apl-source:20
  ناتج = []
  # apl-source:21
  for ك in range(ن):
    # apl-source:22
    ناتج.append(0)
  # apl-source:23
  ي = 0
  # apl-source:24
  ج = ن - 1
  # apl-source:25
  for ك in range(ن - 1, -1, -1):
    # apl-source:26
    if ق[ي] * ق[ي] > ق[ج] * ق[ج]:
      # apl-source:27
      ناتج[ك] = ق[ي] * ق[ي]
      # apl-source:28
      ي = ي + 1
    # apl-source:29
    else:
      # apl-source:30
      ناتج[ك] = ق[ج] * ق[ج]
      # apl-source:31
      ج = ج - 1
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
تأكد_يساوي(مربعات_مرتبة([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100], "خمسة")
# apl-source:35
تأكد_يساوي(مربعات_مرتبة([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121], "أخرى")
# apl-source:36
