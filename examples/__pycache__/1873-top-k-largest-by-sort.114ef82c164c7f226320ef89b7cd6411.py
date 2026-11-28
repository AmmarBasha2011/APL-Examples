
# apl-source:1
# مثال 1873 — أكبر ك عنصراً
# apl-source:2
# Top k largest elements
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1873-top-k-largest-by-sort.apl
# apl-source:6

# apl-source:7
# نرتب تصاعدياً
# apl-source:8
# نقلب النهاية
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
def أكبر_ك(ق, ك):
  # apl-source:19
  ن = ق + []
  # apl-source:20
  ن.sort()
  # apl-source:21
  ن.reverse()
  # apl-source:22
  return ن[:ك]
# apl-source:23

# apl-source:24
تأكد_يساوي(أكبر_ك([3, 1, 4, 1, 5, 9, 2, 6], 3), [9, 6, 5], "ثلاثة")
# apl-source:25
تأكد_يساوي(أكبر_ك([1, 2], 5), [2, 1], "أكثر من الطول")
# apl-source:26
تأكد_يساوي(أكبر_ك([7], 1), [7], "واحد")
# apl-source:27
