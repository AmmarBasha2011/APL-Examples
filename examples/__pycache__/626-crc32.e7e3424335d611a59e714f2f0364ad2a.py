
# apl-source:1
# مثال 626 — مجموع CRC32
# apl-source:2
# CRC32 checksum
# apl-source:3
# Demonstrates: CRC32، بتات، تحقق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/626-crc32.apl
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
# مجموع CRC32 الاختباري بت بت
# apl-source:25
# Demonstrates: كثيرة حدود عكسية, أو-حصري على البتات, قيمة تحقق معيارية
# apl-source:26
# نفس الخوارزمية في zip و PNG و Ethernet
# apl-source:27

# apl-source:28
def كrc32(نص):
  # apl-source:29
  بيانات = نص.encode("utf-8")
  # apl-source:30
  ك = 4294967295
  # apl-source:31
  for بايت in بيانات:
    # apl-source:32
    ك = ك ^ بايت
    # apl-source:33
    for بت in range(8):
      # apl-source:34
      if ك % 2 == 1:
        # apl-source:35
        ك = (ك // 2) ^ 3988292384
      # apl-source:36
      else:
        # apl-source:37
        ك = ك // 2
  # apl-source:38
  return ك ^ 4294967295
# apl-source:39

# apl-source:40
نتيجة = كrc32("123456789")
# apl-source:41
print("CRC32(123456789) =", نتيجة)
# apl-source:42
تأكد_يساوي(نتيجة, 3421780262, "القيمة المعيارية 0xCBF43926")
# apl-source:43
تأكد_يساوي(كrc32(""), 0, "نص فارغ")
# apl-source:44
تأكد_يساوي(كrc32("أ") != كrc32("ب"), True, "حرف مختلف يعطي قيمة مختلفة")
# apl-source:45
