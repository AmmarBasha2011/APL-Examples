
# apl-source:1
# مثال 1052 — حذف التكرار الزائد
# apl-source:2
# Remove duplicates allowing two
# apl-source:3
# Demonstrates: مؤشر كتابة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1052-remove-dup-twice.apl
# apl-source:6

# apl-source:7
# نقبل العنصر لو كان مختلفاً عن العنصر الذي يسبق موضع الكتابة بمكانين
# apl-source:8
# فتبقى كل قيمة مرتين على الأكثر
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
def اثنان_فقط(ق):
  # apl-source:19
  ك = 0
  # apl-source:20
  for س in ق:
    # apl-source:21
    if (ك < 2) or (س != ق[ك - 2]):
      # apl-source:22
      ق[ك] = س
      # apl-source:23
      ك = ك + 1
  # apl-source:24
  return ك
# apl-source:25

# apl-source:26
أ = [1, 1, 1, 2, 2, 3]
# apl-source:27
تأكد_يساوي(اثنان_فقط(أ), 5, "طول أول")
# apl-source:28
تأكد_يساوي(أ[:5], [1, 1, 2, 2, 3], "محتوى أول")
# apl-source:29
ب = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# apl-source:30
تأكد_يساوي(اثنان_فقط(ب), 7, "طول ثان")
# apl-source:31
تأكد_يساوي(ب[:7], [0, 0, 1, 1, 2, 3, 3], "محتوى ثان")
# apl-source:32
