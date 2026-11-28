
# apl-source:1
# مثال 1725 — عدد التبديلات في الفرز بالاختيار
# apl-source:2
# Selection sort swap count
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1725-selection-sort-swap-count.apl
# apl-source:6

# apl-source:7
# نختار أصغر عنصر في كل دورة
# apl-source:8
# نبدل فقط عند اختلاف الموضع
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
def تبديلات_الاختيار(ق):
  # apl-source:19
  ق = ق + []
  # apl-source:20
  عد = 0
  # apl-source:21
  for ي in range(len(ق)):
    # apl-source:22
    صغير = ي
    # apl-source:23
    for ك in range(ي + 1, len(ق)):
      # apl-source:24
      if ق[ك] < ق[صغير]:
        # apl-source:25
        صغير = ك
    # apl-source:26
    if صغير != ي:
      # apl-source:27
      ت = ق[ي]
      # apl-source:28
      ق[ي] = ق[صغير]
      # apl-source:29
      ق[صغير] = ت
      # apl-source:30
      عد = عد + 1
  # apl-source:31
  return عد
# apl-source:32

# apl-source:33
تأكد_يساوي(تبديلات_الاختيار([1, 2, 3]), 0, "مرتبة")
# apl-source:34
تأكد_يساوي(تبديلات_الاختيار([3, 2, 1]), 1, "معكوسة")
# apl-source:35
تأكد_يساوي(تبديلات_الاختيار([4, 3, 2, 1]), 2, "أربعة")
# apl-source:36
