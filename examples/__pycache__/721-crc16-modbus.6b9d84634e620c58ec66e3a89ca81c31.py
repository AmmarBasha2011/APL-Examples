
# apl-source:1
# مثال 721 — CRC-16 مودباس
# apl-source:2
# CRC-16 Modbus
# apl-source:3
# Demonstrates: بتات LSB أولاً، متعددة حدود، انزياح
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/721-crc16-modbus.apl
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
# CRC-16/MODBUS: كشف أخطاء في الشبكات الصناعية
# apl-source:25
# Demonstrates: كثيرة حدود منعكسة A001, إزاحة بتية, قيمة ابتدائية FFFF
# apl-source:26
# فحص معياري: "123456789" يعطي 0x4B37
# apl-source:27

# apl-source:28
def بايتات(نص):
  # apl-source:29
  ناتج = []
  # apl-source:30
  for ي in range(len(نص)):
    # apl-source:31
    ناتج.append(ord(نص[ي]) % 256)
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
def crc16(بايتات):
  # apl-source:35
  crc = 65535
  # apl-source:36
  for بايت in بايتات:
    # apl-source:37
    crc = crc ^ بايت
    # apl-source:38
    for بت in range(8):
      # apl-source:39
      if crc % 2 == 1:
        # apl-source:40
        crc = (crc // 2) ^ 40961
      # apl-source:41
      else:
        # apl-source:42
        crc = crc // 2
  # apl-source:43
  return crc
# apl-source:44

# apl-source:45
تأكد_يساوي(crc16(بايتات("123456789")), 19255, "فحص 4B37 القياسي")
# apl-source:46
تأكد_يساوي(crc16(بايتات("")), 65535, "الفارغ يبقى FFFF")
# apl-source:47
تأكد_يساوي(crc16(بايتات("A")), 28799, "حرف واحد")
# apl-source:48
تأكد_يساوي(crc16(بايتات("abc")) != crc16(بايتات("abd")), True, "حرف يغير")
# apl-source:49
تأكد_يساوي(crc16(بايتات("abc")) != crc16(بايتات("acb")), True, "الترتيب يهم")
# apl-source:50
# إعادة الإرسال: إلحاق CRC ثم الحساب يعطي صفرا
# apl-source:51
بيانات = بايتات("test")
# apl-source:52
crc = crc16(بيانات)
# apl-source:53
مع_تحقق = بيانات + [crc % 256, crc // 256]
# apl-source:54
تأكد_يساوي(crc16(مع_تحقق), 0, "البيانات مع CRC تصفر")
# apl-source:55
print("crc(123456789):", crc16(بايتات("123456789")))
# apl-source:56
