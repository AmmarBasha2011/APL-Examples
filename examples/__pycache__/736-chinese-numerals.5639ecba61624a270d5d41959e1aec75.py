
# apl-source:1
# مثال 736 — أرقام صينية
# apl-source:2
# Chinese numerals
# apl-source:3
# Demonstrates: منازل عشرية، صفر وسيط، عشرات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/736-chinese-numerals.apl
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
# الأرقام الصينية: تحويل 0..999 إلى حروف صينية
# apl-source:25
# Demonstrates: تفكيك منازل عشرية, قاعدة الصفر الوسيط 零, عشرات بلا 一 للعشرة
# apl-source:26
# 10..19 تكتب 十.. بلا 一 بادئة, والصفر بين منزلتين يظهر كـ 零
# apl-source:27

# apl-source:28
أرقام = "零一二三四五六七八九"
# apl-source:29

# apl-source:30
def رقم(د):
  # apl-source:31
  return أرقام[د]
# apl-source:32

# apl-source:33
def إلى_صيني(عدد):
  # apl-source:34
  if عدد == 0:
    # apl-source:35
    return "零"
  # apl-source:36
  مئات = عدد // 100
  # apl-source:37
  باقي = عدد % 100
  # apl-source:38
  عشرات = باقي // 10
  # apl-source:39
  آحاد = باقي % 10
  # apl-source:40
  ناتج = ""
  # apl-source:41
  if مئات > 0:
    # apl-source:42
    ناتج = ناتج + رقم(مئات) + "百"
  # apl-source:43
  if عشرات == 0 and آحاد > 0 and مئات > 0:
    # apl-source:44
    ناتج = ناتج + "零"
  # apl-source:45
  if عشرات > 0:
    # apl-source:46
    if عشرات == 1 and مئات == 0:
      # apl-source:47
      ناتج = ناتج + "十"
    # apl-source:48
    else:
      # apl-source:49
      ناتج = ناتج + رقم(عشرات) + "十"
  # apl-source:50
  if آحاد > 0:
    # apl-source:51
    ناتج = ناتج + رقم(آحاد)
  # apl-source:52
  return ناتج
# apl-source:53

# apl-source:54
تأكد_يساوي(إلى_صيني(0), "零", "صفر")
# apl-source:55
تأكد_يساوي(إلى_صيني(7), "七", "سبعة")
# apl-source:56
تأكد_يساوي(إلى_صيني(10), "十", "عشرة بلا واحد")
# apl-source:57
تأكد_يساوي(إلى_صيني(15), "十五", "خمسة عشر")
# apl-source:58
تأكد_يساوي(إلى_صيني(23), "二十三", "ثلاثة وعشرون")
# apl-source:59
تأكد_يساوي(إلى_صيني(58), "五十八", "ثمانية وخمسون")
# apl-source:60
تأكد_يساوي(إلى_صيني(100), "一百", "مئة")
# apl-source:61
تأكد_يساوي(إلى_صيني(105), "一百零五", "صفر وسيط")
# apl-source:62
تأكد_يساوي(إلى_صيني(110), "一百一十", "مئة وعشرة")
# apl-source:63
تأكد_يساوي(إلى_صيني(306), "三百零六", "ثلاثمئة وستة")
# apl-source:64
تأكد_يساوي(إلى_صيني(520), "五百二十", "خمسمئة وعشرون")
# apl-source:65
تأكد_يساوي(إلى_صيني(999), "九百九十九", "تسعمئة وتسعة وتسعون")
# apl-source:66

# apl-source:67
print("42 =", إلى_صيني(42))
# apl-source:68
print("202 =", إلى_صيني(202))
# apl-source:69
