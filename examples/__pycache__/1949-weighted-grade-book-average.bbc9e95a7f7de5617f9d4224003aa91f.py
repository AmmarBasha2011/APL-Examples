
# apl-source:1
# مثال 1949 — المعدل المرجح لدرجات المواد
# apl-source:2
# Weighted grade average
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1949-weighted-grade-book-average.apl
# apl-source:6

# apl-source:7
# # نستخدم أعدادا صحيحة ونقسم مرة واحدة في النهاية
# apl-source:8
# # نرجع المعدل مقربا لمنزلتين
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
def معدل(درجات, اوزان):
  # apl-source:19
  بسط = 0
  # apl-source:20
  مقام = 0
  # apl-source:21
  for ك in range(len(درجات)):
    # apl-source:22
    بسط = بسط + درجات[ك] * اوزان[ك]
    # apl-source:23
    مقام = مقام + اوزان[ك]
  # apl-source:24
  return round(بسط / مقام, 2)
# apl-source:25

# apl-source:26
تأكد_يساوي(معدل([90, 80, 70], [3, 2, 1]), 83.33, "ثلاث مواد")
# apl-source:27
تأكد_يساوي(معدل([100], [4]), 100.0, "مادة واحدة")
# apl-source:28
تأكد_يساوي(معدل([60, 80], [1, 1]), 70.0, "وزنان متساويان")
# apl-source:29
