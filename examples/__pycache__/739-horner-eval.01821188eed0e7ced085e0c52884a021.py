
# apl-source:1
# مثال 739 — طريقة هورنر
# apl-source:2
# Horner's method
# apl-source:3
# Demonstrates: طي معاملات، اشتقاق، كفاءة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/739-horner-eval.apl
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
# تقييم كثيرات الحدود بطريقة هورنر
# apl-source:25
# Demonstrates: طي المعاملات, اشتقاق قائمة معاملات, عدد عمليات أدنى
# apl-source:26
# هورنر يقيّم بـ ن ضربة فقط بدل حساب كل قوة على حدة
# apl-source:27

# apl-source:28
def هورنر(معاملات, س):
  # apl-source:29
  ناتج = 0
  # apl-source:30
  for أ in معاملات:
    # apl-source:31
    ناتج = ناتج * س + أ
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
def اشتق(معاملات):
  # apl-source:35
  ن = len(معاملات) - 1
  # apl-source:36
  ناتج = []
  # apl-source:37
  for ي in range(ن):
    # apl-source:38
    ناتج.append(معاملات[ي] * (ن - ي))
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
def قيمة_ومشتقة(معاملات, س):
  # apl-source:42
  return [هورنر(معاملات, س), هورنر(اشتق(معاملات), س)]
# apl-source:43

# apl-source:44
كثير = [2, -6, 2, -1]
# apl-source:45

# apl-source:46
تأكد_يساوي(هورنر(كثير, 3), 5, "عند 3")
# apl-source:47
تأكد_يساوي(هورنر(كثير, 0), -1, "الحد الثابت")
# apl-source:48
تأكد_يساوي(هورنر(كثير, 1), -3, "عند 1")
# apl-source:49
تأكد_يساوي(هورنر([1, 0, -2], 5), 23, "س^2 ناقص 2 عند 5")
# apl-source:50
تأكد_يساوي(هورنر([7], 99), 7, "ثابت فقط")
# apl-source:51

# apl-source:52
تأكد_يساوي(اشتق(كثير), [6, -12, 2], "معاملات المشتقة")
# apl-source:53
تأكد_يساوي(اشتق([1, 0, -2]), [2, 0], "مشتقة س^2-2")
# apl-source:54
تأكد_يساوي(اشتق([5]), [], "مشتقة الثابت فارغة")
# apl-source:55

# apl-source:56
تأكد_يساوي(قيمة_ومشتقة(كثير, 3), [5, 20], "قيمة ومشتقة معاً")
# apl-source:57
تأكد_يساوي(هورنر(اشتق(اشتق(كثير)), 3), 24, "المشتقة الثانية")
# apl-source:58

# apl-source:59
print("p(3) =", هورنر(كثير, 3))
# apl-source:60
print("p'(3) =", هورنر(اشتق(كثير), 3))
# apl-source:61
