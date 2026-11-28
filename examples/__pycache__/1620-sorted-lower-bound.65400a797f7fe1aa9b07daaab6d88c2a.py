
# apl-source:1
# مثال 1620 — الحد الأدنى للإدراج
# apl-source:2
# Lower bound in a sorted list
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1620-sorted-lower-bound.apl
# apl-source:6

# apl-source:7
# نبحث عن أول عنصر أكبر أو يساوي
# apl-source:8
# النتيجة قد تساوي طول القائمة
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
def حد_أدنى(أ, هدف):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = len(أ)
  # apl-source:21
  while ي < ج:
    # apl-source:22
    م = (ي + ج) // 2
    # apl-source:23
    if أ[م] < هدف:
      # apl-source:24
      ي = م + 1
    # apl-source:25
    else:
      # apl-source:26
      ج = م
  # apl-source:27
  return ي
# apl-source:28

# apl-source:29
تأكد_يساوي(حد_أدنى([1, 2, 4, 4, 6], 4), 2, "أول أربعة")
# apl-source:30
تأكد_يساوي(حد_أدنى([1, 2, 4, 4, 6], 5), 4, "بين قيمتين")
# apl-source:31
تأكد_يساوي(حد_أدنى([1, 2], 9), 2, "بعد الكل")
# apl-source:32
