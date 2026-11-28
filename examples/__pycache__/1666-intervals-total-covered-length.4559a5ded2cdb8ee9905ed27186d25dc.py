
# apl-source:1
# مثال 1666 — الطول الكلي المغطى بالفترات
# apl-source:2
# Total length covered by intervals
# apl-source:3
# Demonstrates: فترات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1666-intervals-total-covered-length.apl
# apl-source:6

# apl-source:7
# نرتب الفترات بالبداية
# apl-source:8
# نمدد الفترة الحالية عند التداخل
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
def طول_مغطى(فترات):
  # apl-source:19
  ف = []
  # apl-source:20
  for ع in فترات:
    # apl-source:21
    ف.append([ع[0], ع[1]])
  # apl-source:22
  ف.sort()
  # apl-source:23
  مجموع = 0
  # apl-source:24
  بداية = ف[0][0]
  # apl-source:25
  نهاية = ف[0][1]
  # apl-source:26
  for ع in ف:
    # apl-source:27
    if ع[0] > نهاية:
      # apl-source:28
      مجموع = مجموع + نهاية - بداية
      # apl-source:29
      بداية = ع[0]
      # apl-source:30
      نهاية = ع[1]
    # apl-source:31
    else:
      # apl-source:32
      if ع[1] > نهاية:
        # apl-source:33
        نهاية = ع[1]
  # apl-source:34
  مجموع = مجموع + نهاية - بداية
  # apl-source:35
  return مجموع
# apl-source:36

# apl-source:37
تأكد_يساوي(طول_مغطى([[1, 4], [2, 6], [8, 10]]), 7, "تداخل وانفصال")
# apl-source:38
تأكد_يساوي(طول_مغطى([[0, 5]]), 5, "فترة واحدة")
# apl-source:39
تأكد_يساوي(طول_مغطى([[1, 2], [2, 3], [3, 4]]), 3, "متلاصقة")
# apl-source:40
