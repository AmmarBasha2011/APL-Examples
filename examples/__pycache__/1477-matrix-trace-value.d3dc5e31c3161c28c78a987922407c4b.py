
# apl-source:1
# مثال 1477 — أثر المصفوفة
# apl-source:2
# Matrix trace
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1477-matrix-trace-value.apl
# apl-source:6

# apl-source:7
# الأثر معرف للمصفوفات المربعة
# apl-source:8
# نجمع العنصر عند كل ع,ع
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
def الأثر(م):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ع in range(len(م)):
    # apl-source:21
    مجموع = مجموع + م[ع][ع]
  # apl-source:22
  return مجموع
# apl-source:23

# apl-source:24
تأكد_يساوي(الأثر([[1, 2], [3, 4]]), 5, "اثنان")
# apl-source:25
تأكد_يساوي(الأثر([[2, 0, 0], [0, 3, 0], [0, 0, 4]]), 9, "قطرية")
# apl-source:26
تأكد_يساوي(الأثر([[7]]), 7, "واحدة")
# apl-source:27
