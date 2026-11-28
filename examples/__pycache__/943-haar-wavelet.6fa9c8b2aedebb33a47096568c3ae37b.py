
# apl-source:1
# مثال 943 — مويجة هار
# apl-source:2
# Haar wavelet
# apl-source:3
# Demonstrates: متوسطات وفروق متدرجة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/943-haar-wavelet.apl
# apl-source:6

# apl-source:7
# تحويل هار المويجي: متوسطات وفروق متدرجة المستويات
# apl-source:8
# أبسط مويجة: ضغط وكشف حواف الإشارات
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
def هار(إشارة):
  # apl-source:19
  جارية = []
  # apl-source:20
  for x in إشارة:
    # apl-source:21
    جارية = جارية + [x]
  # apl-source:22
  فروق = []
  # apl-source:23
  while len(جارية) > 1:
    # apl-source:24
    متوسطات = []
    # apl-source:25
    فروق_مستوى = []
    # apl-source:26
    for i in range(0, len(جارية), 2):
      # apl-source:27
      متوسطات = متوسطات + [(جارية[i] + جارية[i + 1]) / 2]
      # apl-source:28
      فروق_مستوى = فروق_مستوى + [(جارية[i] - جارية[i + 1]) / 2]
    # apl-source:29
    # أحدث الفروق في المقدمة
    # apl-source:30
    فروق = فروق_مستوى + فروق
    # apl-source:31
    جارية = متوسطات
  # apl-source:32
  return جارية + فروق
# apl-source:33

# apl-source:34
نتيجة = هار([4, 6, 10, 12, 8, 6, 5, 5])
# apl-source:35
print("المعاملات:", نتيجة)
# apl-source:36

# apl-source:37
متوقع = [7, 1, -3, 1, -1, -1, 1, 0]
# apl-source:38
تأكد_يساوي(len(نتيجة), 8, "الطول محفوظ")
# apl-source:39
for i in range(8):
  # apl-source:40
  تأكد_يساوي(round(نتيجة[i], 6), متوقع[i], "معامل " + str(i))
# apl-source:41

# apl-source:42
# المعامل الأول هو متوسط الإشارة الكلي
# apl-source:43
تأكد_يساوي(round(نتيجة[0], 6), 7, "المتوسط الكلي")
# apl-source:44

# apl-source:45
# إشارة ثابتة: كل الفروق صفر
# apl-source:46
ثابتة = هار([3, 3, 3, 3])
# apl-source:47
تأكد_يساوي(round(ثابتة[0], 6), 3, "متوسط ثابتة")
# apl-source:48
تأكد_يساوي(round(ثابتة[1], 6), 0, "فرق صفري 1")
# apl-source:49
تأكد_يساوي(round(ثابتة[3], 6), 0, "فرق صفري 3")
# apl-source:50
