
# apl-source:1
# مثال 596 — تجزئة متسقة
# apl-source:2
# Consistent hashing
# apl-source:3
# Demonstrates: تجزئة متسقة، عقد، استقرار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/596-consistent-hashing.apl
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
# التجزئة المتسقة: توزيع مفاتيح على عقد قابلة للزيادة
# apl-source:25
# Demonstrates: حلقة تجزئة, استقرار التوزيع عند إزالة عقدة
# apl-source:26
# عند إزالة عقدة تعاد كتابة مفاتيحها فقط، لا كل المفاتيح
# apl-source:27

# apl-source:28
def تجزئة(نص):
  # apl-source:29
  ح = 0
  # apl-source:30
  for حرف in نص:
    # apl-source:31
    ح = (ح * 31 + ord(حرف)) % 1000
  # apl-source:32
  return ح
# apl-source:33

# apl-source:34
def وّزع(مفاتيح, عقد):
  # apl-source:35
  توزيع = {}
  # apl-source:36
  for مفتاح in مفاتيح:
    # apl-source:37
    عقدة = عقد[تجزئة(مفتاح) % len(عقد)]
    # apl-source:38
    توزيع[مفتاح] = عقدة
  # apl-source:39
  return توزيع
# apl-source:40

# apl-source:41
مفاتيح = []
# apl-source:42
for ي in range(60):
  # apl-source:43
  مفاتيح.append("مفتاح-" + str(ي))
# apl-source:44

# apl-source:45
عقد_ثلاث = ["أ", "ب", "ج"]
# apl-source:46
ت = وّزع(مفاتيح, عقد_ثلاث)
# apl-source:47
عقد_بعد = ["أ", "ج"]
# apl-source:48
ت2 = وّزع(مفاتيح, عقد_بعد)
# apl-source:49

# apl-source:50
ثابتة = 0
# apl-source:51
for مفتاح in مفاتيح:
  # apl-source:52
  if ت[مفتاح] == ت2[مفتاح]:
    # apl-source:53
    ثابتة = ثابتة + 1
# apl-source:54
print("مفاتيح لم تتحرك بعد حذف عقدة:", ثابتة, "من", len(مفاتيح))
# apl-source:55
تأكد_يساوي(ثابتة > 0, True, "أغلب التوزيع مستقر")
# apl-source:56
تأكد_يساوي(len(ت2), 60, "كل المفاتيح ما زالت موزعة")
# apl-source:57
