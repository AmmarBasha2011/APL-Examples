
# apl-source:1
# مثال 1847 — حذف عنصر والاحتفاظ بالعدد
# apl-source:2
# Remove element and return new length
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1847-remove-element-in-place-count.apl
# apl-source:6

# apl-source:7
# مؤشر كتابة ومؤشر قراءة
# apl-source:8
# نعيد الطول الجديد
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
  كتابة = 0
  # apl-source:20
  for قراءة in range(len(ق)):
    # apl-source:21
    if ق[قراءة] != قيمة:
      # apl-source:22
      ق[كتابة] = ق[قراءة]
      # apl-source:23
      كتابة = كتابة + 1
  # apl-source:24
  return كتابة
# apl-source:25

# apl-source:26
أ = [3, 2, 2, 3]
# apl-source:27
ن = احذف(أ, 3)
# apl-source:28
تأكد_يساوي(ن, 2, "الطول")
# apl-source:29
تأكد_يساوي(أ[:ن], [2, 2], "المحتوى")
# apl-source:30
ب = [0, 1, 2, 2, 3, 0, 4, 2]
# apl-source:31
تأكد_يساوي(احذف(ب, 2), 5, "ثمانية")
# apl-source:32
