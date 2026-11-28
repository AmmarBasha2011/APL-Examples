
# apl-source:1
# مثال 1041 — أول وآخر موضع
# apl-source:2
# First and last position in sorted array
# apl-source:3
# Demonstrates: بحثان ثنائيان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1041-first-last-position.apl
# apl-source:6

# apl-source:7
# نبحث عن أول موضع لا تقل قيمته عن الهدف
# apl-source:8
# وعن أول موضع أكبر منه، والفرق بينهما نطاق الظهور
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
def حد_ادنى(ق, هدف):
  # apl-source:19
  ي = 0
  # apl-source:20
  ل = len(ق)
  # apl-source:21
  while ي < ل:
    # apl-source:22
    وسط = (ي + ل) // 2
    # apl-source:23
    if ق[وسط] < هدف:
      # apl-source:24
      ي = وسط + 1
    # apl-source:25
    else:
      # apl-source:26
      ل = وسط
  # apl-source:27
  return ي
# apl-source:28

# apl-source:29
def مدى(ق, هدف):
  # apl-source:30
  أول = حد_ادنى(ق, هدف)
  # apl-source:31
  if (أول == len(ق)) or (ق[أول] != هدف):
    # apl-source:32
    return [-1, -1]
  # apl-source:33
  return [أول, حد_ادنى(ق, هدف + 1) - 1]
# apl-source:34

# apl-source:35
تأكد_يساوي(مدى([5, 7, 7, 8, 8, 10], 8), [3, 4], "ظهوران")
# apl-source:36
تأكد_يساوي(مدى([5, 7, 7, 8, 8, 10], 6), [-1, -1], "غائب")
# apl-source:37
تأكد_يساوي(مدى([], 1), [-1, -1], "فارغة")
# apl-source:38
تأكد_يساوي(مدى([2, 2], 2), [0, 1], "الكل")
# apl-source:39
