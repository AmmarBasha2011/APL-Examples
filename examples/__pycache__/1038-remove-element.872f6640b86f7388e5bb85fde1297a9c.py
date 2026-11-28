
# apl-source:1
# مثال 1038 — حذف قيمة من القائمة
# apl-source:2
# Remove element in place
# apl-source:3
# Demonstrates: مؤشر كتابة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1038-remove-element.apl
# apl-source:6

# apl-source:7
# نمر على القائمة وننسخ العناصر المختلفة عن القيمة للأمام
# apl-source:8
# ونرجع عدد العناصر المتبقية
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
def احذف(ق, قيمة):
  # apl-source:19
  ك = 0
  # apl-source:20
  for ع in range(len(ق)):
    # apl-source:21
    if ق[ع] != قيمة:
      # apl-source:22
      ق[ك] = ق[ع]
      # apl-source:23
      ك = ك + 1
  # apl-source:24
  return ك
# apl-source:25

# apl-source:26
أ = [3, 2, 2, 3]
# apl-source:27
تأكد_يساوي(احذف(أ, 3), 2, "طول بعد الحذف")
# apl-source:28
تأكد_يساوي(أ[:2], [2, 2], "المتبقي")
# apl-source:29
ب = [0, 1, 2, 2, 3, 0, 4, 2]
# apl-source:30
تأكد_يساوي(احذف(ب, 2), 5, "حذف الاثنين")
# apl-source:31
تأكد_يساوي(احذف([1, 1], 1), 0, "حذف الكل")
# apl-source:32
