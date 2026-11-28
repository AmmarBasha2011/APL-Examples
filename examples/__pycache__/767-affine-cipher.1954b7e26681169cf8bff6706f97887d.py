
# apl-source:1
# مثال 767 — الشفرة الخطية
# apl-source:2
# Affine cipher
# apl-source:3
# Demonstrates: (ax+b) mod 26، معكوس ضربي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/767-affine-cipher.apl
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
# الشفرة الخطية: E(x) = (ax + b) mod 26
# apl-source:25
# Demonstrates: معكوس ضربي مودولو, شرط التشارك الأولي gcd(a,26)=1
# apl-source:26

# apl-source:27
def عاكس_ضربي(أ):
  # apl-source:28
  for ي in range(1, 26):
    # apl-source:29
    if (أ * ي) % 26 == 1:
      # apl-source:30
      return ي
  # apl-source:31
  return 0
# apl-source:32

# apl-source:33
def تشفير_خطي(نص, أ, ب):
  # apl-source:34
  ناتج = ""
  # apl-source:35
  for حرف in نص:
    # apl-source:36
    if حرف == " ":
      # apl-source:37
      ناتج = ناتج + " "
    # apl-source:38
    else:
      # apl-source:39
      ناتج = ناتج + chr((أ * (ord(حرف) - 65) + ب) % 26 + 65)
  # apl-source:40
  return ناتج
# apl-source:41

# apl-source:42
def فك_خطي(نص, أ, ب):
  # apl-source:43
  عاكس = عاكس_ضربي(أ)
  # apl-source:44
  ناتج = ""
  # apl-source:45
  for حرف in نص:
    # apl-source:46
    if حرف == " ":
      # apl-source:47
      ناتج = ناتج + " "
    # apl-source:48
    else:
      # apl-source:49
      ناتج = ناتج + chr((عاكس * (ord(حرف) - 65 - ب)) % 26 + 65)
  # apl-source:50
  return ناتج
# apl-source:51

# apl-source:52
تأكد_يساوي(عاكس_ضربي(5), 21, "معكوس 5 هو 21")
# apl-source:53
تأكد_يساوي(تشفير_خطي("AFFINECIPHER", 5, 8), "IHHWVCSWFRCP", "متجه ويكيبيديا الخطية")
# apl-source:54
تأكد_يساوي(تشفير_خطي("HELLO WORLD", 5, 8), "RCLLA OAPLX", "تشفير مع فراغ")
# apl-source:55
تأكد_يساوي(فك_خطي("IHHWVCSWFRCP", 5, 8), "AFFINECIPHER", "فك الخطية")
# apl-source:56
تأكد_يساوي(فك_خطي(تشفير_خطي("CRYPTOGRAPHY", 7, 3), 7, 3), "CRYPTOGRAPHY", "ذهاب وإياب بمفتاح آخر")
# apl-source:57
