
# apl-source:1
# مثال 1759 — حقيبة الظهر صفر واحد
# apl-source:2
# 0/1 knapsack max value
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1759-knapsack-zero-one-value.apl
# apl-source:6

# apl-source:7
# جدول بحسب السعة
# apl-source:8
# نحدث من الأكبر للأصغر
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
def حقيبة(أوزان, قيم, سعة):
  # apl-source:19
  أفضل = []
  # apl-source:20
  for ك in range(سعة + 1):
    # apl-source:21
    أفضل.append(0)
  # apl-source:22
  for ي in range(len(أوزان)):
    # apl-source:23
    س = سعة
    # apl-source:24
    while س >= أوزان[ي]:
      # apl-source:25
      أفضل[س] = max(أفضل[س], أفضل[س - أوزان[ي]] + قيم[ي])
      # apl-source:26
      س = س - 1
  # apl-source:27
  return أفضل[سعة]
# apl-source:28

# apl-source:29
تأكد_يساوي(حقيبة([1, 3, 4, 5], [1, 4, 5, 7], 7), 9, "كلاسيكية")
# apl-source:30
تأكد_يساوي(حقيبة([5], [10], 3), 0, "لا تتسع")
# apl-source:31
تأكد_يساوي(حقيبة([2, 3], [3, 4], 5), 7, "الكل")
# apl-source:32
