
# apl-source:1
# مثال 811 — ألوان الويب
# apl-source:2
# Hex colors & WCAG
# apl-source:3
# Demonstrates: sRGB خطي، إضاءة، تباين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/811-hex-color.apl
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
# ألوان الويب: تحويل hex إلى RGB وحساب الإضاءة ونسبة التباين WCAG
# apl-source:25
# Demonstrates: تحليل خانات سداسية, خطية قناة sRGB, نسبة تباين معيارية
# apl-source:26

# apl-source:27
سداسي = "0123456789abcdef"
# apl-source:28

# apl-source:29
def قيمة_خانة(ح):
  # apl-source:30
  for ي in range(16):
    # apl-source:31
    if سداسي[ي] == ح:
      # apl-source:32
      return ي
  # apl-source:33
  return 0
# apl-source:34

# apl-source:35
def حلل_لون(لون):
  # apl-source:36
  خالص = لون
  # apl-source:37
  if لون[0] == "#":
    # apl-source:38
    خالص = لون[1:7]
  # apl-source:39
  قيم = []
  # apl-source:40
  for ي in range(3):
    # apl-source:41
    قيم.append(قيمة_خانة(خالص[ي * 2]) * 16 + قيمة_خانة(خالص[ي * 2 + 1]))
  # apl-source:42
  return قيم
# apl-source:43

# apl-source:44
def خطية(قناة):
  # apl-source:45
  ج = قناة / 255.0
  # apl-source:46
  if ج <= 0.03928:
    # apl-source:47
    return ج / 12.92
  # apl-source:48
  return ((ج + 0.055) / 1.055) ** 2.4
# apl-source:49

# apl-source:50
def إضاءة(قيم):
  # apl-source:51
  return 0.2126 * خطية(قيم[0]) + 0.7152 * خطية(قيم[1]) + 0.0722 * خطية(قيم[2])
# apl-source:52

# apl-source:53
def تباين(لون1, لون2):
  # apl-source:54
  إ1 = إضاءة(حلل_لون(لون1))
  # apl-source:55
  إ2 = إضاءة(حلل_لون(لون2))
  # apl-source:56
  if إ1 < إ2:
    # apl-source:57
    مؤقت = إ1
    # apl-source:58
    إ1 = إ2
    # apl-source:59
    إ2 = مؤقت
  # apl-source:60
  return (إ1 + 0.05) / (إ2 + 0.05)
# apl-source:61

# apl-source:62
تأكد_يساوي(حلل_لون("#1e80ff"), [30, 128, 255], "تحليل أزرق")
# apl-source:63
تأكد_يساوي(حلل_لون("ffffff"), [255, 255, 255], "بدون شباك")
# apl-source:64
تأكد_يساوي(round(إضاءة([255, 255, 255]), 4), 1.0, "إضاءة الأبيض")
# apl-source:65
تأكد_يساوي(round(إضاءة([30, 128, 255]), 4), 0.2293, "إضاءة الأزرق")
# apl-source:66
تأكد_يساوي(round(تباين("#000000", "#ffffff"), 2), 21.0, "أعلى تباين")
# apl-source:67
تأكد_يساوي(round(تباين("#1e80ff", "#ffffff"), 2), 3.76, "أزرق على أبيض")
# apl-source:68
تأكد_يساوي(round(تباين("#767676", "#ffffff"), 2), 4.54, "رمادي AA")
# apl-source:69
