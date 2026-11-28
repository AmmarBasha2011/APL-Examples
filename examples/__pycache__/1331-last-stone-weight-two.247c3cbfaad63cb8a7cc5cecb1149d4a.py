
# apl-source:1
# مثال 1331 — وزن الحجر الأخير
# apl-source:2
# Last stone weight II
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1331-last-stone-weight-two.apl
# apl-source:6

# apl-source:7
# نقسم الأحجار إلى مجموعتين بأقل فرق
# apl-source:8
# نبحث عن أكبر مجموع ممكن لا يتجاوز نصف الكل
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
def حجر_اخير(أحجار):
  # apl-source:19
  كل = 0
  # apl-source:20
  for ح in أحجار:
    # apl-source:21
    كل = كل + ح
  # apl-source:22
  نصف = كل // 2
  # apl-source:23
  ممكن = [False] * (نصف + 1)
  # apl-source:24
  ممكن[0] = True
  # apl-source:25
  for ح in أحجار:
    # apl-source:26
    for ع in range(نصف, ح - 1, -1):
      # apl-source:27
      if ممكن[ع - ح]:
        # apl-source:28
        ممكن[ع] = True
  # apl-source:29
  for ع in range(نصف, -1, -1):
    # apl-source:30
    if ممكن[ع]:
      # apl-source:31
      return كل - 2 * ع
  # apl-source:32
  return كل
# apl-source:33

# apl-source:34
تأكد_يساوي(حجر_اخير([2,7,4,1,8,1]), 1, "واحد")
# apl-source:35
تأكد_يساوي(حجر_اخير([31,26,33,21,40]), 5, "خمسة")
# apl-source:36
تأكد_يساوي(حجر_اخير([1]), 1, "حجر")
# apl-source:37
