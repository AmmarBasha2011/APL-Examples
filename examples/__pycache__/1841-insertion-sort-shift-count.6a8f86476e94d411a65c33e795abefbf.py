
# apl-source:1
# مثال 1841 — عدد الإزاحات في الفرز بالإدراج
# apl-source:2
# Insertion sort shift count
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1841-insertion-sort-shift-count.apl
# apl-source:6

# apl-source:7
# كل إزاحة تعني انعكاساً واحداً
# apl-source:8
# نمرر العنصر لموضعه
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
def إزاحات(ق):
  # apl-source:19
  ق = ق + []
  # apl-source:20
  عد = 0
  # apl-source:21
  for ي in range(1, len(ق)):
    # apl-source:22
    مفتاح = ق[ي]
    # apl-source:23
    ك = ي - 1
    # apl-source:24
    while ك >= 0 and ق[ك] > مفتاح:
      # apl-source:25
      ق[ك + 1] = ق[ك]
      # apl-source:26
      ك = ك - 1
      # apl-source:27
      عد = عد + 1
    # apl-source:28
    ق[ك + 1] = مفتاح
  # apl-source:29
  return عد
# apl-source:30

# apl-source:31
تأكد_يساوي(إزاحات([1, 2, 3]), 0, "مرتبة")
# apl-source:32
تأكد_يساوي(إزاحات([3, 2, 1]), 3, "معكوسة")
# apl-source:33
تأكد_يساوي(إزاحات([2, 1, 3, 1]), 3, "مختلطة")
# apl-source:34
