
# apl-source:1
# مثال 816 — تجزئة روبن هود
# apl-source:2
# Robin Hood hashing
# apl-source:3
# Demonstrates: معالجة مفتوحة، تبادل بالمسافة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/816-robin-hood-hashing.apl
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
# تجزئة روبن هود: معالجة مفتوحة مع سرقة من الأغنياء للفقراء
# apl-source:25
# Demonstrates: مسافة من البيت الأصلي, تبادل عند تجاوز المسافة, بحث بإيقاف مبكر
# apl-source:26

# apl-source:27
حجم = 16
# apl-source:28

# apl-source:29
def جدول_جديد():
  # apl-source:30
  جدول = []
  # apl-source:31
  for ي in range(حجم):
    # apl-source:32
    جدول.append([-1, 0])
  # apl-source:33
  return جدول
# apl-source:34

# apl-source:35
def أدخل(جدول, مفتاح):
  # apl-source:36
  موضع = مفتاح % حجم
  # apl-source:37
  حالي = مفتاح
  # apl-source:38
  مسافة = 0
  # apl-source:39
  while 1 == 1:
    # apl-source:40
    if جدول[موضع][0] == -1:
      # apl-source:41
      جدول[موضع][0] = حالي
      # apl-source:42
      جدول[موضع][1] = مسافة
      # apl-source:43
      return موضع
    # apl-source:44
    if جدول[موضع][1] < مسافة:
      # apl-source:45
      مؤقت1 = جدول[موضع][0]
      # apl-source:46
      مؤقت2 = جدول[موضع][1]
      # apl-source:47
      جدول[موضع][0] = حالي
      # apl-source:48
      جدول[موضع][1] = مسافة
      # apl-source:49
      حالي = مؤقت1
      # apl-source:50
      مسافة = مؤقت2
    # apl-source:51
    موضع = (موضع + 1) % حجم
    # apl-source:52
    مسافة = مسافة + 1
# apl-source:53

# apl-source:54
def ابحث(جدول, مفتاح):
  # apl-source:55
  موضع = مفتاح % حجم
  # apl-source:56
  مسافة = 0
  # apl-source:57
  while جدول[موضع][0] != -1:
    # apl-source:58
    if جدول[موضع][0] == مفتاح:
      # apl-source:59
      return موضع
    # apl-source:60
    if جدول[موضع][1] < مسافة:
      # apl-source:61
      return -1
    # apl-source:62
    موضع = (موضع + 1) % حجم
    # apl-source:63
    مسافة = مسافة + 1
  # apl-source:64
  return -1
# apl-source:65

# apl-source:66
جدول = جدول_جديد()
# apl-source:67
أدخل(جدول, 5)
# apl-source:68
أدخل(جدول, 18)
# apl-source:69
أدخل(جدول, 20)
# apl-source:70
أدخل(جدول, 37)
# apl-source:71
تأكد_يساوي(جدول[5][0], 5, "خمسة في بيتها")
# apl-source:72
تأكد_يساوي(جدول[2][0], 18, "ثمانية عشر")
# apl-source:73
تأكد_يساوي(جدول[6][0], 37, "سبعة وثلاثون أزاحت")
# apl-source:74
تأكد_يساوي(جدول[6][1], 1, "مسافة واحدة")
# apl-source:75
تأكد_يساوي(ابحث(جدول, 20), 4, "بحث ناجح")
# apl-source:76
تأكد_يساوي(ابحث(جدول, 99), -1, "بحث فاشل بإيقاف مبكر")
# apl-source:77
