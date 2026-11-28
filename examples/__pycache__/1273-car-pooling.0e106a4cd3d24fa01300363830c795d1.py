
# apl-source:1
# مثال 1273 — مشاركة السيارة
# apl-source:2
# Car pooling capacity
# apl-source:3
# Demonstrates: فروق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1273-car-pooling.apl
# apl-source:6

# apl-source:7
# نضيف الركاب عند الصعود ونطرحهم عند النزول
# apl-source:8
# ونتحقق أن العدد لا يتجاوز السعة
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
def تكفي(رحلات, سعة):
  # apl-source:19
  تغير = [0] * 1001
  # apl-source:20
  for ر in رحلات:
    # apl-source:21
    تغير[ر[1]] = تغير[ر[1]] + ر[0]
    # apl-source:22
    تغير[ر[2]] = تغير[ر[2]] - ر[0]
  # apl-source:23
  حالي = 0
  # apl-source:24
  for ت in تغير:
    # apl-source:25
    حالي = حالي + ت
    # apl-source:26
    if حالي > سعة:
      # apl-source:27
      return False
  # apl-source:28
  return True
# apl-source:29

# apl-source:30
تأكد_يساوي(تكفي([[2,1,5],[3,3,7]], 4), False, "لا تكفي")
# apl-source:31
تأكد_يساوي(تكفي([[2,1,5],[3,3,7]], 5), True, "تكفي")
# apl-source:32
تأكد_يساوي(تكفي([[3,2,7],[3,7,9],[8,3,9]], 11), True, "ثلاث رحلات")
# apl-source:33
