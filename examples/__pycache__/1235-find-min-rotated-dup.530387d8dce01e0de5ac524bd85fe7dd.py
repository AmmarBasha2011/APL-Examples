
# apl-source:1
# مثال 1235 — أصغر في دوران مع تكرار
# apl-source:2
# Find minimum in rotated sorted array with duplicates
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1235-find-min-rotated-dup.apl
# apl-source:6

# apl-source:7
# لو الوسط أكبر من اليمين فالأصغر يمين
# apl-source:8
# ولو أصغر فهو يسار وإلا نقلص اليمين
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
def اصغر_مدورة(أ):
  # apl-source:19
  ي = 0
  # apl-source:20
  ن = len(أ) - 1
  # apl-source:21
  while ي < ن:
    # apl-source:22
    م = (ي + ن) // 2
    # apl-source:23
    if أ[م] > أ[ن]:
      # apl-source:24
      ي = م + 1
    # apl-source:25
    elif أ[م] < أ[ن]:
      # apl-source:26
      ن = م
    # apl-source:27
    else:
      # apl-source:28
      ن = ن - 1
  # apl-source:29
  return أ[ي]
# apl-source:30

# apl-source:31
تأكد_يساوي(اصغر_مدورة([3,4,5,1,2]), 1, "بلا تكرار")
# apl-source:32
تأكد_يساوي(اصغر_مدورة([2,2,2,0,1]), 0, "مع تكرار")
# apl-source:33
تأكد_يساوي(اصغر_مدورة([1,3,3]), 1, "غير مدورة")
# apl-source:34
تأكد_يساوي(اصغر_مدورة([3,1,3,3,3]), 1, "تكرار محير")
# apl-source:35
