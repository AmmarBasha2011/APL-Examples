
# apl-source:1
# مثال 1039 — بحث في مصفوفة مدورة
# apl-source:2
# Search in rotated sorted array
# apl-source:3
# Demonstrates: بحث ثنائي معدل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1039-search-rotated.apl
# apl-source:6

# apl-source:7
# أحد نصفي القائمة مرتب دائماً
# apl-source:8
# نحدد النصف المرتب ونقرر هل القيمة داخله
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
def ابحث_مدور(ق, هدف):
  # apl-source:19
  ي = 0
  # apl-source:20
  ل = len(ق) - 1
  # apl-source:21
  while ي <= ل:
    # apl-source:22
    وسط = (ي + ل) // 2
    # apl-source:23
    if ق[وسط] == هدف:
      # apl-source:24
      return وسط
    # apl-source:25
    if ق[ي] <= ق[وسط]:
      # apl-source:26
      if (ق[ي] <= هدف) and (هدف < ق[وسط]):
        # apl-source:27
        ل = وسط - 1
      # apl-source:28
      else:
        # apl-source:29
        ي = وسط + 1
    # apl-source:30
    else:
      # apl-source:31
      if (ق[وسط] < هدف) and (هدف <= ق[ل]):
        # apl-source:32
        ي = وسط + 1
      # apl-source:33
      else:
        # apl-source:34
        ل = وسط - 1
  # apl-source:35
  return -1
# apl-source:36

# apl-source:37
تأكد_يساوي(ابحث_مدور([4, 5, 6, 7, 0, 1, 2], 0), 4, "الصفر")
# apl-source:38
تأكد_يساوي(ابحث_مدور([4, 5, 6, 7, 0, 1, 2], 3), -1, "غير موجود")
# apl-source:39
تأكد_يساوي(ابحث_مدور([1], 1), 0, "عنصر واحد")
# apl-source:40
تأكد_يساوي(ابحث_مدور([5, 1, 3], 5), 0, "أول عنصر")
# apl-source:41
