
# apl-source:1
# مثال 835 — كولموغوروف-سميرنوف
# apl-source:2
# Kolmogorov-Smirnov
# apl-source:3
# Demonstrates: توزيع تراكمي تجريبي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/835-kolmogorov-smirnov.apl
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
# إحصاء كولموغوروف-سميرنوف: أقصى انحراف بين التوزيع التجريبي والنظري
# apl-source:25
# Demonstrates: دالة توزيع تراكمية تجريبية, مقارنة بالمنتظم, إحصاء D
# apl-source:26

# apl-source:27
def فرز(قائمة):
  # apl-source:28
  نسخة = []
  # apl-source:29
  for عنصر in قائمة:
    # apl-source:30
    نسخة.append(عنصر)
  # apl-source:31
  for ي in range(len(نسخة)):
    # apl-source:32
    أدنى = ي
    # apl-source:33
    for ج in range(ي + 1, len(نسخة)):
      # apl-source:34
      if نسخة[ج] < نسخة[أدنى]:
        # apl-source:35
        أدنى = ج
    # apl-source:36
    مؤقت = نسخة[ي]
    # apl-source:37
    نسخة[ي] = نسخة[أدنى]
    # apl-source:38
    نسخة[أدنى] = مؤقت
  # apl-source:39
  return نسخة
# apl-source:40

# apl-source:41
def إحصاء_كي_إس(بيانات):
  # apl-source:42
  مرتبة = فرز(بيانات)
  # apl-source:43
  ن = len(مرتبة)
  # apl-source:44
  أقصى = 0.0
  # apl-source:45
  for ي in range(ن):
    # apl-source:46
    أعلى = (ي + 1) / ن - مرتبة[ي]
    # apl-source:47
    if أعلى < 0:
      # apl-source:48
      أعلى = 0 - أعلى
    # apl-source:49
    أدنى = مرتبة[ي] - ي / ن
    # apl-source:50
    if أدنى < 0:
      # apl-source:51
      أدنى = 0 - أدنى
    # apl-source:52
    if أعلى > أقصى:
      # apl-source:53
      أقصى = أعلى
    # apl-source:54
    if أدنى > أقصى:
      # apl-source:55
      أقصى = أدنى
  # apl-source:56
  return أقصى
# apl-source:57

# apl-source:58
تأكد_يساوي(round(إحصاء_كي_إس([0.05, 0.2, 0.35, 0.5, 0.62, 0.78, 0.9, 0.95]), 4), 0.155, "عينة قريبة من المنتظم")
# apl-source:59
تأكد_يساوي(round(إحصاء_كي_إس([0.5, 0.5, 0.5, 0.5]), 4), 0.5, "عينة منحازة")
# apl-source:60
تأكد_يساوي(round(إحصاء_كي_إس([0.125, 0.375, 0.625, 0.875]), 4), 0.125, "أدنى انحراف ممكن")
# apl-source:61
تأكد_يساوي(فرز([3, 1, 2]), [1, 2, 3], "الفرز")
# apl-source:62
