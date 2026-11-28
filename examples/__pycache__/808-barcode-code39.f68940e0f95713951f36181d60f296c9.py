
# apl-source:1
# مثال 808 — باركود Code 39
# apl-source:2
# Code 39 barcode
# apl-source:3
# Demonstrates: تسعة عناصر، نجمتان، mod 43
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/808-barcode-code39.apl
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
# باركود Code 39: تسعة عناصر لكل محرف ثلاثة منها عريضة
# apl-source:25
# Demonstrates: جدول أنماط متوازي, محرف بداية ونهاية, خانة تحقق mod 43
# apl-source:26

# apl-source:27
محارف = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# apl-source:28
أنماط = ["111331311", "311311113", "113311113", "313311111", "111331113", "311331111", "113331111", "111311313", "311311311", "113311311", "311113113", "113113113", "313113111", "111133113", "311133111", "113133111", "111113313", "311113311", "113113311", "111133311", "311111133", "113111133", "313111131", "111131133", "311131131", "113131131", "111111333", "311111331", "113111331", "111131331", "331111113", "133111113", "333111111", "131131113", "331131111", "133131111"]
# apl-source:29
نجمة = "131131311"
# apl-source:30

# apl-source:31
def موقع(ح):
  # apl-source:32
  for ي in range(36):
    # apl-source:33
    if محارف[ي] == ح:
      # apl-source:34
      return ي
  # apl-source:35
  return -1
# apl-source:36

# apl-source:37
def شفر(نص):
  # apl-source:38
  أجزاء = [نجمة]
  # apl-source:39
  for ح in نص:
    # apl-source:40
    if ح == " ":
      # apl-source:41
      أجزاء.append("133111311")
    # apl-source:42
    else:
      # apl-source:43
      أجزاء.append(أنماط[موقع(ح)])
  # apl-source:44
  أجزاء.append(نجمة)
  # apl-source:45
  return "0".join(أجزاء)
# apl-source:46

# apl-source:47
def خانة_تحقق(نص):
  # apl-source:48
  مجموع = 0
  # apl-source:49
  for ح in نص:
    # apl-source:50
    مجموع = مجموع + موقع(ح)
  # apl-source:51
  return محارف[مجموع % 43]
# apl-source:52

# apl-source:53
تأكد_يساوي(موقع("A"), 10, "موقع A")
# apl-source:54
تأكد_يساوي(أنماط[10], "311113113", "نمط A")
# apl-source:55
تأكد_يساوي(شفر("APL"), "1311313110311113113011313113101131111330131131311", "ترميز APL")
# apl-source:56
تأكد_يساوي(خانة_تحقق("APL"), "D", "تحقق APL")
# apl-source:57
تأكد_يساوي(خانة_تحقق("CODE39"), "W", "تحقق CODE39")
# apl-source:58
تأكد_يساوي(len(شفر("A")), 29, "طول محرف واحد مع النجمتين")
# apl-source:59
