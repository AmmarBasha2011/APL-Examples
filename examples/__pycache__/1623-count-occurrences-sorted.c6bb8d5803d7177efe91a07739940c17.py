
# apl-source:1
# مثال 1623 — عدد مرات الظهور في قائمة مرتبة
# apl-source:2
# Count occurrences in sorted list
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1623-count-occurrences-sorted.apl
# apl-source:6

# apl-source:7
# نحسب الحدين بالبحث الثنائي
# apl-source:8
# الفرق هو التكرار
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
def حد(أ, هدف, أعلى):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = len(أ)
  # apl-source:21
  while ي < ج:
    # apl-source:22
    م = (ي + ج) // 2
    # apl-source:23
    if أ[م] < هدف or (أعلى and أ[م] == هدف):
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
def تكرار(أ, هدف):
  # apl-source:30
  return حد(أ, هدف, True) - حد(أ, هدف, False)
# apl-source:31

# apl-source:32
تأكد_يساوي(تكرار([1, 2, 2, 2, 3], 2), 3, "ثلاث")
# apl-source:33
تأكد_يساوي(تكرار([1, 2, 3], 5), 0, "غائب")
# apl-source:34
تأكد_يساوي(تكرار([7, 7], 7), 2, "الكل")
# apl-source:35
