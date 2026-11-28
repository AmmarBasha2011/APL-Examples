
# apl-source:1
# مثال 1830 — بحث ثنائي تكراري
# apl-source:2
# Recursive binary search
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1830-recursive-binary-search-index.apl
# apl-source:6

# apl-source:7
# نقارن بالمنتصف
# apl-source:8
# نستدعي النصف المناسب
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
def ابحث(ق, هدف, يسار, يمين):
  # apl-source:19
  if يسار > يمين:
    # apl-source:20
    return -1
  # apl-source:21
  وسط = (يسار + يمين) // 2
  # apl-source:22
  if ق[وسط] == هدف:
    # apl-source:23
    return وسط
  # apl-source:24
  if ق[وسط] < هدف:
    # apl-source:25
    return ابحث(ق, هدف, وسط + 1, يمين)
  # apl-source:26
  return ابحث(ق, هدف, يسار, وسط - 1)
# apl-source:27

# apl-source:28
ق = [1, 3, 5, 7, 9, 11]
# apl-source:29
تأكد_يساوي(ابحث(ق, 7, 0, 5), 3, "وجد")
# apl-source:30
تأكد_يساوي(ابحث(ق, 4, 0, 5), -1, "لم يوجد")
# apl-source:31
تأكد_يساوي(ابحث(ق, 1, 0, 5), 0, "الأول")
# apl-source:32
