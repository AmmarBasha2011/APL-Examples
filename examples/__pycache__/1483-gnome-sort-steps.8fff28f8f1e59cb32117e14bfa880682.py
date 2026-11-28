
# apl-source:1
# مثال 1483 — الفرز القزمي
# apl-source:2
# Gnome sort
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1483-gnome-sort-steps.apl
# apl-source:6

# apl-source:7
# نتقدم خطوة إذا كان الجاران مرتبين
# apl-source:8
# نبدل ونرجع إذا لم يكونا كذلك
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
def فرز_قزمي(أ):
  # apl-source:19
  ع = 0
  # apl-source:20
  while ع < len(أ):
    # apl-source:21
    if ع == 0 or أ[ع] >= أ[ع - 1]:
      # apl-source:22
      ع = ع + 1
    # apl-source:23
    else:
      # apl-source:24
      ت = أ[ع]
      # apl-source:25
      أ[ع] = أ[ع - 1]
      # apl-source:26
      أ[ع - 1] = ت
      # apl-source:27
      ع = ع - 1
  # apl-source:28
  return أ
# apl-source:29

# apl-source:30
تأكد_يساوي(فرز_قزمي([5, 2, 9, 1]), [1, 2, 5, 9], "عادي")
# apl-source:31
تأكد_يساوي(فرز_قزمي([]), [], "فارغ")
# apl-source:32
تأكد_يساوي(فرز_قزمي([3, 3, 1]), [1, 3, 3], "مكرر")
# apl-source:33
