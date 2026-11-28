
# apl-source:1
# مثال 1592 — مربعات مرتبة
# apl-source:2
# Sorted squares of sorted list
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1592-sorted-squares-two-pointers.apl
# apl-source:6

# apl-source:7
# الأكبر مربعاً عند أحد الطرفين
# apl-source:8
# نملأ الناتج من النهاية
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
def مربعات_مرتبة(أ):
  # apl-source:19
  ن = len(أ)
  # apl-source:20
  ناتج = []
  # apl-source:21
  for ع in range(ن):
    # apl-source:22
    ناتج.append(0)
  # apl-source:23
  ي = 0
  # apl-source:24
  ج = ن - 1
  # apl-source:25
  موضع = ن - 1
  # apl-source:26
  while ي <= ج:
    # apl-source:27
    يس = أ[ي] * أ[ي]
    # apl-source:28
    يم = أ[ج] * أ[ج]
    # apl-source:29
    if يس > يم:
      # apl-source:30
      ناتج[موضع] = يس
      # apl-source:31
      ي = ي + 1
    # apl-source:32
    else:
      # apl-source:33
      ناتج[موضع] = يم
      # apl-source:34
      ج = ج - 1
    # apl-source:35
    موضع = موضع - 1
  # apl-source:36
  return ناتج
# apl-source:37

# apl-source:38
تأكد_يساوي(مربعات_مرتبة([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100], "مختلطة")
# apl-source:39
تأكد_يساوي(مربعات_مرتبة([-3, -2]), [4, 9], "سالبة")
# apl-source:40
تأكد_يساوي(مربعات_مرتبة([]), [], "فارغة")
# apl-source:41
