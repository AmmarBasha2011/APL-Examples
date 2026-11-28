
# apl-source:1
# مثال 1019 — المسارات الفريدة
# apl-source:2
# Unique paths in a grid
# apl-source:3
# Demonstrates: جدول تراكمي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1019-unique-paths.apl
# apl-source:6

# apl-source:7
# روبوت يتحرك يميناً وأسفل فقط
# apl-source:8
# عدد طرق خانة هو مجموع طرق الخانة العليا واليسرى
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
def مسارات(صفوف, اعمدة):
  # apl-source:19
  صف = [1] * اعمدة
  # apl-source:20
  for ر in range(1, صفوف):
    # apl-source:21
    for ع in range(1, اعمدة):
      # apl-source:22
      صف[ع] = صف[ع] + صف[ع - 1]
  # apl-source:23
  return صف[اعمدة - 1]
# apl-source:24

# apl-source:25
تأكد_يساوي(مسارات(3, 7), 28, "ثلاثة في سبعة")
# apl-source:26
تأكد_يساوي(مسارات(3, 2), 3, "ثلاثة في اثنين")
# apl-source:27
تأكد_يساوي(مسارات(1, 5), 1, "صف واحد")
# apl-source:28
تأكد_يساوي(مسارات(10, 10), 48620, "عشرة في عشرة")
# apl-source:29
