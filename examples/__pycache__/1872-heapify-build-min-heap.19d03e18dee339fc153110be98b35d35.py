
# apl-source:1
# مثال 1872 — بناء كومة صغرى من قائمة
# apl-source:2
# Build min heap by sift down
# apl-source:3
# Demonstrates: هياكل بيانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1872-heapify-build-min-heap.apl
# apl-source:6

# apl-source:7
# نبدأ من آخر أب
# apl-source:8
# ننزل العنصر مع الأصغر من ابنيه
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
def انزل(ق, ك):
  # apl-source:19
  ن = len(ق)
  # apl-source:20
  while True:
    # apl-source:21
    صغير = ك
    # apl-source:22
    يسار = 2 * ك + 1
    # apl-source:23
    يمين = 2 * ك + 2
    # apl-source:24
    if يسار < ن and ق[يسار] < ق[صغير]:
      # apl-source:25
      صغير = يسار
    # apl-source:26
    if يمين < ن and ق[يمين] < ق[صغير]:
      # apl-source:27
      صغير = يمين
    # apl-source:28
    if صغير == ك:
      # apl-source:29
      return 0
    # apl-source:30
    ت = ق[ك]
    # apl-source:31
    ق[ك] = ق[صغير]
    # apl-source:32
    ق[صغير] = ت
    # apl-source:33
    ك = صغير
# apl-source:34

# apl-source:35
def ابن_كومة(ق):
  # apl-source:36
  ق = ق + []
  # apl-source:37
  for ك in range(len(ق) // 2 - 1, -1, -1):
    # apl-source:38
    انزل(ق, ك)
  # apl-source:39
  return ق
# apl-source:40

# apl-source:41
ن = ابن_كومة([5, 3, 8, 1, 9, 2])
# apl-source:42
تأكد_يساوي(ن[0], 1, "الجذر الأصغر")
# apl-source:43
تأكد_يساوي(len(ن), 6, "الطول")
# apl-source:44
for ك in range(len(ن)):
  # apl-source:45
  if 2 * ك + 1 < len(ن):
    # apl-source:46
    تأكد_يساوي(ن[ك] <= ن[2 * ك + 1], True, "خاصية الأب")
# apl-source:47
