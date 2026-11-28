
# apl-source:1
# مثال 1628 — عدد دورات قائمة مرتبة
# apl-source:2
# Rotation count of a sorted list
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1628-rotation-count-sorted.apl
# apl-source:6

# apl-source:7
# نقارن الوسط بالنهاية
# apl-source:8
# الأصغر يقع حيث ينكسر الترتيب
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
def عدد_الدورات(أ):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = len(أ) - 1
  # apl-source:21
  while ي < ج:
    # apl-source:22
    م = (ي + ج) // 2
    # apl-source:23
    if أ[م] > أ[ج]:
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
تأكد_يساوي(عدد_الدورات([15, 18, 2, 3, 6, 12]), 2, "اثنتان")
# apl-source:30
تأكد_يساوي(عدد_الدورات([1, 2, 3]), 0, "بلا دوران")
# apl-source:31
تأكد_يساوي(عدد_الدورات([3, 1, 2]), 1, "واحدة")
# apl-source:32
