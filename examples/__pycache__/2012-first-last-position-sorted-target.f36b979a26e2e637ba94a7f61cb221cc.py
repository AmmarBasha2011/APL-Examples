
# apl-source:1
# مثال 2012 — أول وآخر موضع لقيمة في قائمة مرتبة
# apl-source:2
# First and last position
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2012-first-last-position-sorted-target.apl
# apl-source:6

# apl-source:7
# # أول موضع هو الحد الأدنى للقيمة
# apl-source:8
# # وآخر موضع قبل الحد الأدنى للقيمة زائد واحد
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
def حد_ادنى(ق, ه):
  # apl-source:19
  ي = 0
  # apl-source:20
  ل = len(ق)
  # apl-source:21
  while ي < ل:
    # apl-source:22
    وس = (ي + ل) // 2
    # apl-source:23
    if ق[وس] < ه:
      # apl-source:24
      ي = وس + 1
    # apl-source:25
    else:
      # apl-source:26
      ل = وس
  # apl-source:27
  return ي
# apl-source:28

# apl-source:29
def موضعان(ق, ه):
  # apl-source:30
  ا = حد_ادنى(ق, ه)
  # apl-source:31
  if ا == len(ق) or ق[ا] != ه:
    # apl-source:32
    return [-1, -1]
  # apl-source:33
  return [ا, حد_ادنى(ق, ه + 1) - 1]
# apl-source:34

# apl-source:35
تأكد_يساوي(موضعان([5, 7, 7, 8, 8, 10], 8), [3, 4], "٨")
# apl-source:36
تأكد_يساوي(موضعان([5, 7, 7, 8, 8, 10], 6), [-1, -1], "غائب")
# apl-source:37
تأكد_يساوي(موضعان([], 1), [-1, -1], "فارغة")
# apl-source:38
