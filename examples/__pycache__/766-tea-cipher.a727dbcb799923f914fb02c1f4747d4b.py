
# apl-source:1
# مثال 766 — تشفير TEA
# apl-source:2
# TEA block cipher
# apl-source:3
# Demonstrates: 32 دورة فيستل، حساب 32-بت، دلتا
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/766-tea-cipher.apl
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
# تشفير TEA الكتلي: 32 دورة فيستل على كلمتين 32-بت
# apl-source:25
# Demonstrates: حساب 32-بت بالقناع, إزاحات بالضرب والقسمة, مفتاح 128-بت
# apl-source:26

# apl-source:27
def شاي_تشفير(ف0, ف1, ك):
  # apl-source:28
  م = 4294967296
  # apl-source:29
  س = 0
  # apl-source:30
  for ي in range(32):
    # apl-source:31
    س = (س + 2654435769) % م
    # apl-source:32
    ت1 = ((ف1 * 16) % م + ك[0]) % م
    # apl-source:33
    ت2 = (ف1 + س) % م
    # apl-source:34
    ت3 = ((ف1 // 32) + ك[1]) % م
    # apl-source:35
    ف0 = (ف0 + ((ت1 ^ ت2) ^ ت3)) % م
    # apl-source:36
    ع1 = ((ف0 * 16) % م + ك[2]) % م
    # apl-source:37
    ع2 = (ف0 + س) % م
    # apl-source:38
    ع3 = ((ف0 // 32) + ك[3]) % م
    # apl-source:39
    ف1 = (ف1 + ((ع1 ^ ع2) ^ ع3)) % م
  # apl-source:40
  return [ف0, ف1]
# apl-source:41

# apl-source:42
def شاي_فك(ف0, ف1, ك):
  # apl-source:43
  م = 4294967296
  # apl-source:44
  س = (84941944608) % م
  # apl-source:45
  for ي in range(32):
    # apl-source:46
    ع1 = ((ف0 * 16) % م + ك[2]) % م
    # apl-source:47
    ع2 = (ف0 + س) % م
    # apl-source:48
    ع3 = ((ف0 // 32) + ك[3]) % م
    # apl-source:49
    ف1 = (ف1 - ((ع1 ^ ع2) ^ ع3)) % م
    # apl-source:50
    ت1 = ((ف1 * 16) % م + ك[0]) % م
    # apl-source:51
    ت2 = (ف1 + س) % م
    # apl-source:52
    ت3 = ((ف1 // 32) + ك[1]) % م
    # apl-source:53
    ف0 = (ف0 - ((ت1 ^ ت2) ^ ت3)) % م
    # apl-source:54
    س = (س - 2654435769) % م
  # apl-source:55
  return [ف0, ف1]
# apl-source:56

# apl-source:57
ن = شاي_تشفير(0, 0, [0, 0, 0, 0])
# apl-source:58
تأكد_يساوي(ن[0], 1105869322, "TEA صفر/صفر النصف الأول")
# apl-source:59
تأكد_يساوي(ن[1], 2495260992, "TEA صفر/صفر النصف الثاني")
# apl-source:60
ن2 = شاي_تشفير(19088743, 2309737967, [1122867, 1146447479, 2291772091, 3437096703])
# apl-source:61
تأكد_يساوي(ن2[0], 309095314, "TEA متجه ثان أول")
# apl-source:62
تأكد_يساوي(ن2[1], 3227859518, "TEA متجه ثان ثان")
# apl-source:63
م = شاي_فك(309095314, 3227859518, [1122867, 1146447479, 2291772091, 3437096703])
# apl-source:64
تأكد_يساوي(م[0], 19088743, "TEA فك أول")
# apl-source:65
تأكد_يساوي(م[1], 2309737967, "TEA فك ثان")
# apl-source:66
