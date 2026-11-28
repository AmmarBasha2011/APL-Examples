
# apl-source:1
# مثال 1831 — البحث في مصفوفة مدورة
# apl-source:2
# Search in rotated sorted array
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1831-search-rotated-sorted-array.apl
# apl-source:6

# apl-source:7
# أحد النصفين مرتب دائماً
# apl-source:8
# نبحث فيه أو في الآخر
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
  يسار = 0
  # apl-source:20
  يمين = len(ق) - 1
  # apl-source:21
  while يسار <= يمين:
    # apl-source:22
    وسط = (يسار + يمين) // 2
    # apl-source:23
    if ق[وسط] == هدف:
      # apl-source:24
      return وسط
    # apl-source:25
    if ق[يسار] <= ق[وسط]:
      # apl-source:26
      if ق[يسار] <= هدف and هدف < ق[وسط]:
        # apl-source:27
        يمين = وسط - 1
      # apl-source:28
      else:
        # apl-source:29
        يسار = وسط + 1
    # apl-source:30
    else:
      # apl-source:31
      if ق[وسط] < هدف and هدف <= ق[يمين]:
        # apl-source:32
        يسار = وسط + 1
      # apl-source:33
      else:
        # apl-source:34
        يمين = وسط - 1
  # apl-source:35
  return -1
# apl-source:36

# apl-source:37
تأكد_يساوي(ابحث_مدور([4, 5, 6, 7, 0, 1, 2], 0), 4, "صفر")
# apl-source:38
تأكد_يساوي(ابحث_مدور([4, 5, 6, 7, 0, 1, 2], 3), -1, "غائب")
# apl-source:39
تأكد_يساوي(ابحث_مدور([1], 1), 0, "واحد")
# apl-source:40
