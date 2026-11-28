
# apl-source:1
# مثال 1840 — العنصر الأصغر ذو الترتيب ك
# apl-source:2
# Kth smallest in sorted matrix
# apl-source:3
# Demonstrates: بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1840-kth-smallest-in-matrix-sorted.apl
# apl-source:6

# apl-source:7
# نسطح المصفوفة
# apl-source:8
# نأخذ العنصر بالترتيب
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
def ك_الأصغر(م, ك):
  # apl-source:19
  كل = []
  # apl-source:20
  for صف in م:
    # apl-source:21
    for ع in صف:
      # apl-source:22
      كل.append(ع)
  # apl-source:23
  كل.sort()
  # apl-source:24
  return كل[ك - 1]
# apl-source:25

# apl-source:26
م = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
# apl-source:27
تأكد_يساوي(ك_الأصغر(م, 8), 13, "الثامن")
# apl-source:28
تأكد_يساوي(ك_الأصغر(م, 1), 1, "الأول")
# apl-source:29
تأكد_يساوي(ك_الأصغر(م, 9), 15, "الأخير")
# apl-source:30
