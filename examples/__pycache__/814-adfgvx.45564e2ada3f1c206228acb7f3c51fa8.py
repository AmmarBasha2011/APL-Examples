
# apl-source:1
# مثال 814 — شفرة ADFGVX
# apl-source:2
# ADFGVX cipher
# apl-source:3
# Demonstrates: مربع 6x6، نقل عمودي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/814-adfgvx.apl
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
# شفرة ADFGVX الألمانية: استبدال بمربع 6x6 ثم نقل عمودي
# apl-source:25
# Demonstrates: مربع مختلط بالأرقام, تسميات ستة محارف, نقل بترتيب مفتاح
# apl-source:26

# apl-source:27
مربع = "NA1C3H8TB2OME5WRPD4F6G7I9J0KQLSUXVYZ"
# apl-source:28
تسميات = "ADFGVX"
# apl-source:29

# apl-source:30
def موقع_مربع(ح):
  # apl-source:31
  for ي in range(36):
    # apl-source:32
    if مربع[ي] == ح:
      # apl-source:33
      return ي
  # apl-source:34
  return -1
# apl-source:35

# apl-source:36
def استبدال(نص):
  # apl-source:37
  أزواج = ""
  # apl-source:38
  for ح in نص:
    # apl-source:39
    م = موقع_مربع(ح)
    # apl-source:40
    أزواج = أزواج + تسميات[م // 6] + تسميات[م % 6]
  # apl-source:41
  return أزواج
# apl-source:42

# apl-source:43
def ترتيب_مفتاح(مفتاح):
  # apl-source:44
  دلائل = []
  # apl-source:45
  for ي in range(len(مفتاح)):
    # apl-source:46
    دلائل.append(ي)
  # apl-source:47
  for ي in range(len(دلائل)):
    # apl-source:48
    أدنى = ي
    # apl-source:49
    for ج in range(ي + 1, len(دلائل)):
      # apl-source:50
      if مفتاح[دلائل[ج]] < مفتاح[دلائل[أدنى]]:
        # apl-source:51
        أدنى = ج
    # apl-source:52
    مؤقت = دلائل[ي]
    # apl-source:53
    دلائل[ي] = دلائل[أدنى]
    # apl-source:54
    دلائل[أدنى] = مؤقت
  # apl-source:55
  return دلائل
# apl-source:56

# apl-source:57
def شفر(نص, مفتاح):
  # apl-source:58
  أزواج = استبدال(نص)
  # apl-source:59
  ن = len(مفتاح)
  # apl-source:60
  ناتج = ""
  # apl-source:61
  for عمود in ترتيب_مفتاح(مفتاح):
    # apl-source:62
    صف = 0
    # apl-source:63
    while صف * ن + عمود < len(أزواج):
      # apl-source:64
      ناتج = ناتج + أزواج[صف * ن + عمود]
      # apl-source:65
      صف = صف + 1
  # apl-source:66
  return ناتج
# apl-source:67

# apl-source:68
تأكد_يساوي(استبدال("A1"), "ADAF", "استبدال A1")
# apl-source:69
تأكد_يساوي(استبدال("ATTACK"), "ADDDDDADAGVG", "استبدال ATTACK")
# apl-source:70
تأكد_يساوي(شفر("ATTACK", "GOLD"), "DDGADADAVDDG", "تشفير ATTACK")
# apl-source:71
تأكد_يساوي(شفر("HELLO123", "KEY"), "XVXAGAAVVDVFXDFA", "تشفير مع أرقام")
# apl-source:72
تأكد_يساوي(len(شفر("HELLO123", "KEY")), 16, "الطول مضاعف")
# apl-source:73
