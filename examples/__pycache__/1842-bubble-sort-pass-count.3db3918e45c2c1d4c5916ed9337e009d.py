
# apl-source:1
# مثال 1842 — عدد جولات الفرز الفقاعي
# apl-source:2
# Bubble sort passes needed
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1842-bubble-sort-pass-count.apl
# apl-source:6

# apl-source:7
# كل جولة تدفع الأكبر للنهاية
# apl-source:8
# نعد الجولات حتى الاستقرار
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
def جولات(ق):
  # apl-source:19
  ق = ق + []
  # apl-source:20
  عد = 0
  # apl-source:21
  تبدلت = True
  # apl-source:22
  while تبدلت:
    # apl-source:23
    تبدلت = False
    # apl-source:24
    for ك in range(len(ق) - 1):
      # apl-source:25
      if ق[ك] > ق[ك + 1]:
        # apl-source:26
        ت = ق[ك]
        # apl-source:27
        ق[ك] = ق[ك + 1]
        # apl-source:28
        ق[ك + 1] = ت
        # apl-source:29
        تبدلت = True
    # apl-source:30
    if تبدلت:
      # apl-source:31
      عد = عد + 1
  # apl-source:32
  return عد
# apl-source:33

# apl-source:34
تأكد_يساوي(جولات([1, 2, 3]), 0, "مرتبة")
# apl-source:35
تأكد_يساوي(جولات([3, 2, 1]), 2, "معكوسة")
# apl-source:36
تأكد_يساوي(جولات([2, 1]), 1, "اثنان")
# apl-source:37
