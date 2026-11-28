
# apl-source:1
# مثال 1588 — إزالة المكرر من قائمة مرتبة
# apl-source:2
# Remove duplicates from sorted list
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1588-remove-duplicates-sorted-list.apl
# apl-source:6

# apl-source:7
# نقارن كل عنصر بآخر عنصر محفوظ
# apl-source:8
# نضيفه إن اختلف
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
def أزل_المكرر(أ):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in أ:
    # apl-source:21
    if len(ناتج) == 0 or ناتج[len(ناتج) - 1] != ع:
      # apl-source:22
      ناتج.append(ع)
  # apl-source:23
  return ناتج
# apl-source:24

# apl-source:25
تأكد_يساوي(أزل_المكرر([1, 1, 2, 3, 3, 3]), [1, 2, 3], "مكررات")
# apl-source:26
تأكد_يساوي(أزل_المكرر([5, 5]), [5], "قيمة واحدة")
# apl-source:27
تأكد_يساوي(أزل_المكرر([]), [], "فارغة")
# apl-source:28
