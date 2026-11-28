
# apl-source:1
# مثال 1945 — جدولة القرص بطريقة المصعد
# apl-source:2
# Disk scheduling SCAN elevator
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1945-disk-scheduling-scan-elevator-order.apl
# apl-source:6

# apl-source:7
# # نرتب الطلبات الأكبر من الرأس ثم الأصغر منه
# apl-source:8
# # بترتيب تنازلي ونعيد ترتيب الخدمة
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
def ترتيب_الخدمة(طلبات, راس):
  # apl-source:19
  فوق = []
  # apl-source:20
  تحت = []
  # apl-source:21
  for ط in طلبات:
    # apl-source:22
    if ط >= راس:
      # apl-source:23
      فوق = فوق + [ط]
    # apl-source:24
    else:
      # apl-source:25
      تحت = تحت + [ط]
  # apl-source:26
  فوق = sorted(فوق)
  # apl-source:27
  تحت = sorted(تحت)
  # apl-source:28
  خرج = فوق
  # apl-source:29
  for ك in range(len(تحت)):
    # apl-source:30
    خرج = خرج + [تحت[len(تحت) - 1 - ك]]
  # apl-source:31
  return خرج
# apl-source:32

# apl-source:33
تأكد_يساوي(ترتيب_الخدمة([98, 183, 37, 122, 14, 124, 65, 67], 53), [65, 67, 98, 122, 124, 183, 37, 14], "كلاسيكي")
# apl-source:34
تأكد_يساوي(ترتيب_الخدمة([5, 1], 10), [5, 1], "كلها تحت")
# apl-source:35
تأكد_يساوي(ترتيب_الخدمة([20, 30], 10), [20, 30], "كلها فوق")
# apl-source:36
