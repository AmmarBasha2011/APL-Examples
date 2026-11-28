
# apl-source:1
# مثال 1672 — عدد الانعكاسات في المصفوفة
# apl-source:2
# Count inversions in an array
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1672-count-inversions-pairs.apl
# apl-source:6

# apl-source:7
# نقارن كل زوج
# apl-source:8
# ننتبه لترتيب المواضع
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
def انعكاسات(ق):
  # apl-source:19
  عد = 0
  # apl-source:20
  for ي in range(len(ق)):
    # apl-source:21
    for ك in range(ي + 1, len(ق)):
      # apl-source:22
      if ق[ي] > ق[ك]:
        # apl-source:23
        عد = عد + 1
  # apl-source:24
  return عد
# apl-source:25

# apl-source:26
تأكد_يساوي(انعكاسات([1, 2, 3]), 0, "مرتبة")
# apl-source:27
تأكد_يساوي(انعكاسات([3, 2, 1]), 3, "معكوسة")
# apl-source:28
تأكد_يساوي(انعكاسات([2, 4, 1, 3, 5]), 3, "مختلطة")
# apl-source:29
