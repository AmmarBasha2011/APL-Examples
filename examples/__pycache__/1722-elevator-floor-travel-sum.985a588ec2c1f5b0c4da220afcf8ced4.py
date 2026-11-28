
# apl-source:1
# مثال 1722 — مجموع حركة المصعد
# apl-source:2
# Elevator total floors travelled
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1722-elevator-floor-travel-sum.apl
# apl-source:6

# apl-source:7
# يبدأ من الطابق صفر
# apl-source:8
# كل طلب يضيف المسافة
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
def حركة(طلبات):
  # apl-source:19
  موضع = 0
  # apl-source:20
  مجموع = 0
  # apl-source:21
  for ط in طلبات:
    # apl-source:22
    if ط > موضع:
      # apl-source:23
      مجموع = مجموع + ط - موضع
    # apl-source:24
    else:
      # apl-source:25
      مجموع = مجموع + موضع - ط
    # apl-source:26
    موضع = ط
  # apl-source:27
  return مجموع
# apl-source:28

# apl-source:29
تأكد_يساوي(حركة([3, 1, 5]), 9, "ثلاثة")
# apl-source:30
تأكد_يساوي(حركة([]), 0, "لا طلب")
# apl-source:31
تأكد_يساوي(حركة([0, 0]), 0, "ثابت")
# apl-source:32
