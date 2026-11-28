
# apl-source:1
# مثال 2057 — الفرز بالاختيار مع عد المقارنات
# apl-source:2
# Selection sort comparisons
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2057-selection-sort-compare-count.apl
# apl-source:6

# apl-source:7
# # في كل جولة نبحث عن أصغر عنصر
# apl-source:8
# # المقارنات n(n-1)/2 دائما
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
def افرز(ق):
  # apl-source:19
  ق = ق[:]
  # apl-source:20
  مقارنات = 0
  # apl-source:21
  for ك in range(len(ق)):
    # apl-source:22
    ص = ك
    # apl-source:23
    for ي in range(ك + 1, len(ق)):
      # apl-source:24
      مقارنات = مقارنات + 1
      # apl-source:25
      if ق[ي] < ق[ص]:
        # apl-source:26
        ص = ي
    # apl-source:27
    ت = ق[ك]
    # apl-source:28
    ق[ك] = ق[ص]
    # apl-source:29
    ق[ص] = ت
  # apl-source:30
  return [ق, مقارنات]
# apl-source:31

# apl-source:32
تأكد_يساوي(افرز([5, 4, 3]), [[3, 4, 5], 3], "ثلاثة")
# apl-source:33
تأكد_يساوي(افرز([1, 2, 3, 4])[1], 6, "أربعة")
# apl-source:34
تأكد_يساوي(افرز([])[0], [], "فارغة")
# apl-source:35
