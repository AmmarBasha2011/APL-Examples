
# apl-source:1
# مثال 855 — ط بلايبنتز
# apl-source:2
# Leibniz series for pi
# apl-source:3
# Demonstrates: متناوبة، تقارب بطيء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/855-gregory-pi.apl
# apl-source:6

# apl-source:7
# متسلسلة غريغوري-لايبنتز: ط/4 = 1 - 1/3 + 1/5 - 1/7 + ...
# apl-source:8
# أبسط متسلسلة لط لكنها الأبطأ تقارباً
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
def ط_لايبنتز(حدود):
  # apl-source:19
  مجموع = 0.0
  # apl-source:20
  for ك in range(حدود):
    # apl-source:21
    حد = 1.0 / (2 * ك + 1)
    # apl-source:22
    if ك % 2 == 1:
      # apl-source:23
      حد = -حد
    # apl-source:24
    مجموع = مجموع + حد
  # apl-source:25
  return مجموع * 4.0
# apl-source:26

# apl-source:27
ط = ط_لايبنتز(10000)
# apl-source:28
print("ط بعد 10000 حد:", ط)
# apl-source:29

# apl-source:30
تأكد_يساوي(round(ط, 2), 3.14, "خانتان عشريتان صحيحتان")
# apl-source:31
تأكد_يساوي(round(ط, 3), 3.141, "ثلاث خانات")
# apl-source:32

# apl-source:33
# التقارب متناوب: الحد الفردي يقلل والزوجي يزيد
# apl-source:34
ط9 = ط_لايبنتز(9)
# apl-source:35
ط10 = ط_لايبنتز(10)
# apl-source:36
تأكد_يساوي(ط9 > ط10, 1 == 1, "التقارب متناوب حول القيمة")
# apl-source:37
