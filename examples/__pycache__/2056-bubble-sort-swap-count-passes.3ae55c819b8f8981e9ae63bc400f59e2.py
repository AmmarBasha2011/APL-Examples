
# apl-source:1
# مثال 2056 — الفرز الفقاعي مع عد التبديلات
# apl-source:2
# Bubble sort swap count
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2056-bubble-sort-swap-count-passes.apl
# apl-source:6

# apl-source:7
# # نكرر المرور حتى لا يحدث تبديل
# apl-source:8
# # التبديلات تساوي الانقلابات
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
def تبديلات(ق):
  # apl-source:19
  ق = ق[:]
  # apl-source:20
  عدد = 0
  # apl-source:21
  تغير = True
  # apl-source:22
  while تغير:
    # apl-source:23
    تغير = False
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
        عدد = عدد + 1
        # apl-source:30
        تغير = True
  # apl-source:31
  return عدد
# apl-source:32

# apl-source:33
تأكد_يساوي(تبديلات([4, 3, 2, 1]), 6, "معكوسة")
# apl-source:34
تأكد_يساوي(تبديلات([1, 2]), 0, "مرتبة")
# apl-source:35
تأكد_يساوي(تبديلات([2, 1, 3]), 1, "واحد")
# apl-source:36
