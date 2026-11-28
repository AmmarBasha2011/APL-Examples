
# apl-source:1
# مثال 2055 — الفرز بالإدراج مع عد الإزاحات
# apl-source:2
# Insertion sort shift count
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2055-insertion-sort-count-shifts.apl
# apl-source:6

# apl-source:7
# # نعد كم مرة أزحنا عنصرا لليمين
# apl-source:8
# # هذا العدد يساوي عدد الانقلابات
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
def ازاحات(ق):
  # apl-source:19
  ق = ق[:]
  # apl-source:20
  عدد = 0
  # apl-source:21
  for ك in range(1, len(ق)):
    # apl-source:22
    قيمة = ق[ك]
    # apl-source:23
    ي = ك - 1
    # apl-source:24
    while ي >= 0 and ق[ي] > قيمة:
      # apl-source:25
      ق[ي + 1] = ق[ي]
      # apl-source:26
      ي = ي - 1
      # apl-source:27
      عدد = عدد + 1
    # apl-source:28
    ق[ي + 1] = قيمة
  # apl-source:29
  return عدد
# apl-source:30

# apl-source:31
تأكد_يساوي(ازاحات([3, 1, 2]), 2, "٣١٢")
# apl-source:32
تأكد_يساوي(ازاحات([1, 2, 3]), 0, "مرتبة")
# apl-source:33
تأكد_يساوي(ازاحات([3, 2, 1]), 3, "معكوسة")
# apl-source:34
تأكد_يساوي(ازاحات([5, 2, 4, 6, 1, 3]), 9, "ستة")
# apl-source:35
