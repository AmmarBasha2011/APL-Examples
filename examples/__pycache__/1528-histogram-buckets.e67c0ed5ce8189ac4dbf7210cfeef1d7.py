
# apl-source:1
# مثال 1528 — مدرج تكراري
# apl-source:2
# Histogram buckets
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1528-histogram-buckets.apl
# apl-source:6

# apl-source:7
# رقم المجال = القيمة ÷ العرض
# apl-source:8
# نزيد عداد ذلك المجال
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
def مدرج(أ, عرض):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ع in أ:
    # apl-source:21
    مجال = ع // عرض
    # apl-source:22
    عد[مجال] = عد.get(مجال, 0) + 1
  # apl-source:23
  return عد
# apl-source:24

# apl-source:25
تأكد_يساوي(مدرج([1, 5, 12, 15, 18, 25], 10), {0: 2, 1: 3, 2: 1}, "عشرة")
# apl-source:26
تأكد_يساوي(مدرج([3, 3, 3], 5), {0: 3}, "مجال واحد")
# apl-source:27
تأكد_يساوي(مدرج([], 5), {}, "فارغة")
# apl-source:28
