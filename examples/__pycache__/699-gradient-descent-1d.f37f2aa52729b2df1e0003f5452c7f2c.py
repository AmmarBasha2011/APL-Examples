
# apl-source:1
# مثال 699 — النزول التدرجي الأحادي
# apl-source:2
# 1D gradient descent
# apl-source:3
# Demonstrates: مشتقة، معدل تعلم، تذبذب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/699-gradient-descent-1d.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# النزول التدرجي أحادي البعد
# apl-source:25
# Demonstrates: مشتقة, معدل تعلم, تقارب أسي
# apl-source:26
# الهدف: أصغر قيمة لـ (س-3)^2 + 1 عند س=3
# apl-source:27

# apl-source:28
def هدف(س):
  # apl-source:29
  فرق = س - 3.0
  # apl-source:30
  return فرق * فرق + 1.0
# apl-source:31

# apl-source:32
def مشتقة(س):
  # apl-source:33
  return 2.0 * (س - 3.0)
# apl-source:34

# apl-source:35
def انزل(بداية, معدل, خطوات):
  # apl-source:36
  س = بداية
  # apl-source:37
  for ي in range(خطوات):
    # apl-source:38
    س = س - معدل * مشتقة(س)
  # apl-source:39
  return س
# apl-source:40

# apl-source:41
تأكد_يساوي(round(انزل(0.0, 0.1, 60), 3), 3.0, "يتقارب إلى 3")
# apl-source:42
تأكد_يساوي(round(هدف(انزل(0.0, 0.1, 60)), 3), 1.0, "القيمة الدنيا 1")
# apl-source:43
تأكد_يساوي(مشتقة(5.0), 4.0, "مشتقة عند 5")
# apl-source:44
تأكد_يساوي(مشتقة(3.0), 0.0, "مشتقة عند الحل صفر")
# apl-source:45
قفزة = انزل(0.0, 1.0, 3)
# apl-source:46
تأكد_يساوي(round(قفزة, 4), 6.0, "خطوة كبيرة تتذبذب")
# apl-source:47
بطيء = انزل(0.0, 0.01, 10)
# apl-source:48
تأكد_يساوي(بطيء < 1.0, True, "معدل صغير يزحف")
# apl-source:49
print("الحل:", انزل(0.0, 0.1, 60))
# apl-source:50
