
# apl-source:1
# مثال 638 — جدولة القرص بالمصعد
# apl-source:2
# Disk SCAN scheduling
# apl-source:3
# Demonstrates: SCAN، مصعد، ذراع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/638-disk-scan.apl
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
# جدولة القرص بخوارزمية المصعد (SCAN)
# apl-source:25
# Demonstrates: حركة ذراع اتجاهية, خدمة بالطريق, حساب الحركة الكلية
# apl-source:26
# الذراع تخدم الطلبات باتجاهها ثم تنعكس
# apl-source:27

# apl-source:28
def مصعد(طلبات, بداية, اتجاه_أعلى, أقصى_أسطوانة):
  # apl-source:29
  أقل = []
  # apl-source:30
  أعلى = []
  # apl-source:31
  for ط in طلبات:
    # apl-source:32
    if ط < بداية:
      # apl-source:33
      أقل.append(ط)
    # apl-source:34
    else:
      # apl-source:35
      أعلى.append(ط)
  # apl-source:36
  أقل.sort()
  # apl-source:37
  أعلى.sort()
  # apl-source:38
  ترتيب = []
  # apl-source:39
  if اتجاه_أعلى:
    # apl-source:40
    ترتيب = أعلى + [أقصى_أسطوانة] + أقل[::-1]
  # apl-source:41
  else:
    # apl-source:42
    ترتيب = أقل[::-1] + [0] + أعلى
  # apl-source:43
  حركة = 0
  # apl-source:44
  موضع = بداية
  # apl-source:45
  for محطة in ترتيب:
    # apl-source:46
    حركة = حركة + max(محطة - موضع, موضع - محطة)
    # apl-source:47
    موضع = محطة
  # apl-source:48
  return [ترتيب, حركة]
# apl-source:49

# apl-source:50
طلبات = [98, 183, 37, 122, 14, 124, 65, 67]
# apl-source:51
نتيجة = مصعد(طلبات, 53, True, 199)
# apl-source:52
print("الترتيب:", نتيجة[0])
# apl-source:53
print("الحركة الكلية:", نتيجة[1])
# apl-source:54
تأكد_يساوي(نتيجة[0], [65, 67, 98, 122, 124, 183, 199, 37, 14], "ترتيب المصعد صعودا")
# apl-source:55
تأكد_يساوي(نتيجة[1], 331, "حركة 331 أسطوانة")
# apl-source:56
