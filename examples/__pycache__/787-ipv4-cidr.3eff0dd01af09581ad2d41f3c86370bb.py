
# apl-source:1
# مثال 787 — عناوين IPv4 وCIDR
# apl-source:2
# IPv4 and CIDR
# apl-source:3
# Demonstrates: قناع بادئة، شبكة وبث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/787-ipv4-cidr.apl
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
# عناوين IPv4 وCIDR: تحويل، تحقق، مطابقة شبكة، حساب الشبكات الفرعية
# apl-source:25
# Demonstrates: عنوان 32-بت, قناع بادئة, عنوان الشبكة والبث
# apl-source:26

# apl-source:27
def عنوان_عدد(نص):
  # apl-source:28
  أجزاء = نص.split(".")
  # apl-source:29
  if len(أجزاء) != 4:
    # apl-source:30
    return -1
  # apl-source:31
  عدد = 0
  # apl-source:32
  for جزء in أجزاء:
    # apl-source:33
    if len(جزء) == 0:
      # apl-source:34
      return -1
    # apl-source:35
    for حرف in جزء:
      # apl-source:36
      if حرف < "0" or حرف > "9":
        # apl-source:37
        return -1
    # apl-source:38
    ق = int(جزء)
    # apl-source:39
    if ق > 255:
      # apl-source:40
      return -1
    # apl-source:41
    عدد = عدد * 256 + ق
  # apl-source:42
  return عدد
# apl-source:43

# apl-source:44
def عدد_عنوان(عدد):
  # apl-source:45
  أ = (عدد // 16777216) % 256
  # apl-source:46
  ب = (عدد // 65536) % 256
  # apl-source:47
  ج = (عدد // 256) % 256
  # apl-source:48
  د = عدد % 256
  # apl-source:49
  return str(أ) + "." + str(ب) + "." + str(ج) + "." + str(د)
# apl-source:50

# apl-source:51
def قناع(بتات):
  # apl-source:52
  if بتات == 0:
    # apl-source:53
    return 0
  # apl-source:54
  return (4294967296 - قوة2(32 - بتات)) % 4294967296
# apl-source:55

# apl-source:56
def قوة2(ن):
  # apl-source:57
  ق = 1
  # apl-source:58
  for ي in range(ن):
    # apl-source:59
    ق = ق * 2
  # apl-source:60
  return ق
# apl-source:61

# apl-source:62
def في_شبكة(عنوان, شبكة):
  # apl-source:63
  أجزاء = شبكة.split("/")
  # apl-source:64
  أساس = عنوان_عدد(أجزاء[0])
  # apl-source:65
  بتات = int(أجزاء[1])
  # apl-source:66
  ق = قناع(بتات)
  # apl-source:67
  return (عنوان_عدد(عنوان) & ق) == (أساس & ق)
# apl-source:68

# apl-source:69
تأكد_يساوي(عنوان_عدد("192.168.1.5"), 3232235781, "عنوان إلى عدد")
# apl-source:70
تأكد_يساوي(عدد_عنوان(3232235781), "192.168.1.5", "عدد إلى عنوان")
# apl-source:71
تأكد_يساوي(عنوان_عدد("256.1.1.1"), -1, "مقطة فاسدة")
# apl-source:72
تأكد_يساوي(عنوان_عدد("1.2.3"), -1, "ثلاث مقطوعات")
# apl-source:73
تأكد_يساوي(في_شبكة("192.168.1.5", "192.168.1.0/24"), True, "داخل /24")
# apl-source:74
تأكد_يساوي(في_شبكة("192.168.2.5", "192.168.1.0/24"), False, "خارج /24")
# apl-source:75
تأكد_يساوي(في_شبكة("10.0.0.1", "10.0.0.0/8"), True, "داخل /8")
# apl-source:76
ق26 = قناع(26)
# apl-source:77
شبكة = 3232235776 & ق26
# apl-source:78
تأكد_يساوي(عدد_عنوان(شبكة), "192.168.1.0", "شبكة /26")
# apl-source:79
بث = شبكة | (4294967295 ^ ق26)
# apl-source:80
تأكد_يساوي(عدد_عنوان(بث), "192.168.1.63", "بث /26")
# apl-source:81
تأكد_يساوي(قوة2(6) - 2, 62, "مضيفو /26")
# apl-source:82
