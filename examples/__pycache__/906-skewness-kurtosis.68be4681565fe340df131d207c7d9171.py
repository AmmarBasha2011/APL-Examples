
# apl-source:1
# مثال 906 — الالتواء والتفرطح
# apl-source:2
# Skewness and kurtosis
# apl-source:3
# Demonstrates: علات مركزية معيارية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/906-skewness-kurtosis.apl
# apl-source:6

# apl-source:7
# الالتواء والتفرطح: العلتان الثالثة والرابعة للتوزيع
# apl-source:8
# الالتواء يقيس عدم التماثل والتفرطح ثقل الأذيال
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
def وسط(قيم):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for x in قيم:
    # apl-source:21
    مجموع = مجموع + x
  # apl-source:22
  return مجموع / len(قيم)
# apl-source:23

# apl-source:24
def علة_مركزية(قيم, رتبة):
  # apl-source:25
  م = وسط(قيم)
  # apl-source:26
  مجموع = 0
  # apl-source:27
  for x in قيم:
    # apl-source:28
    مجموع = مجموع + (x - م) ** رتبة
  # apl-source:29
  return مجموع / len(قيم)
# apl-source:30

# apl-source:31
def التواء(قيم):
  # apl-source:32
  ع2 = علة_مركزية(قيم, 2)
  # apl-source:33
  ع3 = علة_مركزية(قيم, 3)
  # apl-source:34
  return ع3 / ع2 ** 1.5
# apl-source:35

# apl-source:36
def تفرطح(قيم):
  # apl-source:37
  ع2 = علة_مركزية(قيم, 2)
  # apl-source:38
  ع4 = علة_مركزية(قيم, 4)
  # apl-source:39
  return ع4 / ع2 ** 2 - 3
# apl-source:40

# apl-source:41
قيم = [1, 2, 3, 4, 10]
# apl-source:42
التواء_ق = التواء(قيم)
# apl-source:43
تفرطح_ق = تفرطح(قيم)
# apl-source:44
print("الالتواء:", التواء_ق)
# apl-source:45
print("التفرطح الزائد:", تفرطح_ق)
# apl-source:46

# apl-source:47
# القيمة المتطرفة 10 تسحب الذيل يميناً: التواء موجب
# apl-source:48
تأكد_يساوي(round(التواء_ق, 4), 1.1384, "التواء موجب")
# apl-source:49
تأكد_يساوي(round(تفرطح_ق, 3), -0.212, "تفرطح")
# apl-source:50

# apl-source:51
# التوزيع المتماثل التواؤه صفر
# apl-source:52
تأكد_يساوي(round(التواء([1, 2, 3, 4, 5]), 9), 0, "متماثل")
# apl-source:53
