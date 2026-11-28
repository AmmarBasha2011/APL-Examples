
# apl-source:1
# مثال 4781 — عدد الإزاحات في الترتيب بالإدراج
# apl-source:2
# Insertion sort shift count
# apl-source:3
# Demonstrates: أرقام وخوارزميات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4781-insertion-shifts.apl
# apl-source:6

# apl-source:7
# نأخذ العنصر ونزيح الأكبر منه لليمين
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ق):
  # apl-source:18
  ق = ق + []
  # apl-source:19
  ع = 0
  # apl-source:20
  for ر in range(1, len(ق)):
    # apl-source:21
    ك = ق[ر]
    # apl-source:22
    ي = ر - 1
    # apl-source:23
    while ي >= 0 and ق[ي] > ك:
      # apl-source:24
      ق[ي + 1] = ق[ي]
      # apl-source:25
      ي = ي - 1
      # apl-source:26
      ع = ع + 1
    # apl-source:27
    ق[ي + 1] = ك
  # apl-source:28
  return ع
# apl-source:29

# apl-source:30
تأكد_يساوي(ف([3, 1, 2]), 2, "حالة 1")
# apl-source:31
تأكد_يساوي(ف([1, 2, 3]), 0, "حالة 2")
# apl-source:32
تأكد_يساوي(ف([4, 3, 2, 1]), 6, "حالة 3")
# apl-source:33
تأكد_يساوي(ف([5, 1, 4, 2, 3]), 6, "حالة 4")
# apl-source:34
تأكد_يساوي(ف([]), 0, "حالة 5")
# apl-source:35
