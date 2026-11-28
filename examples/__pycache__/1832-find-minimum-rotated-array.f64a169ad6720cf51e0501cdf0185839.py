
# apl-source:1
# مثال 1832 — أصغر عنصر في مصفوفة مدورة
# apl-source:2
# Minimum in rotated sorted array
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1832-find-minimum-rotated-array.apl
# apl-source:6

# apl-source:7
# إن كان المنتصف أكبر من النهاية فالأصغر يمين
# apl-source:8
# وإلا فهو في اليسار
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
def أصغر_مدور(ق):
  # apl-source:19
  يسار = 0
  # apl-source:20
  يمين = len(ق) - 1
  # apl-source:21
  while يسار < يمين:
    # apl-source:22
    وسط = (يسار + يمين) // 2
    # apl-source:23
    if ق[وسط] > ق[يمين]:
      # apl-source:24
      يسار = وسط + 1
    # apl-source:25
    else:
      # apl-source:26
      يمين = وسط
  # apl-source:27
  return ق[يسار]
# apl-source:28

# apl-source:29
تأكد_يساوي(أصغر_مدور([3, 4, 5, 1, 2]), 1, "خمسة")
# apl-source:30
تأكد_يساوي(أصغر_مدور([4, 5, 6, 7, 0, 1, 2]), 0, "سبعة")
# apl-source:31
تأكد_يساوي(أصغر_مدور([1, 2, 3]), 1, "غير مدورة")
# apl-source:32
