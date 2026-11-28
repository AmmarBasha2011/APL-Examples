
# apl-source:1
# مثال 801 — منسق printf
# apl-source:2
# printf formatter
# apl-source:3
# Demonstrates: %d و%s و%x، حشو أصفار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/801-printf-format.apl
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
# منسق بأسلوب printf: مواضع %d و%s و%x مع حشو بالأصفار
# apl-source:25
# Demonstrates: تحليل محارف التنسيق, تحويل لسداسي يدوياً, حشو بعرض ثابت
# apl-source:26

# apl-source:27
سداسي = "0123456789abcdef"
# apl-source:28

# apl-source:29
def سداسي_نص(ن):
  # apl-source:30
  if ن == 0:
    # apl-source:31
    return "0"
  # apl-source:32
  ناتج = ""
  # apl-source:33
  م = ن
  # apl-source:34
  while م > 0:
    # apl-source:35
    ناتج = سداسي[م % 16] + ناتج
    # apl-source:36
    م = م // 16
  # apl-source:37
  return ناتج
# apl-source:38

# apl-source:39
def تنسيق(قالب, وسائط):
  # apl-source:40
  ناتج = ""
  # apl-source:41
  مؤشر = 0
  # apl-source:42
  ي = 0
  # apl-source:43
  while ي < len(قالب):
    # apl-source:44
    if قالب[ي] == "%":
      # apl-source:45
      if قالب[ي + 1] == "%":
        # apl-source:46
        ناتج = ناتج + "%"
        # apl-source:47
        ي = ي + 2
      # apl-source:48
      else:
        # apl-source:49
        ي = ي + 1
        # apl-source:50
        حشو = " "
        # apl-source:51
        if قالب[ي] == "0":
          # apl-source:52
          حشو = "0"
          # apl-source:53
          ي = ي + 1
        # apl-source:54
        عرض = 0
        # apl-source:55
        while ي < len(قالب) and قالب[ي] >= "0" and قالب[ي] <= "9":
          # apl-source:56
          عرض = عرض * 10 + int(قالب[ي])
          # apl-source:57
          ي = ي + 1
        # apl-source:58
        محرف = قالب[ي]
        # apl-source:59
        قيمة = ""
        # apl-source:60
        if محرف == "d":
          # apl-source:61
          قيمة = str(وسائط[مؤشر])
        # apl-source:62
        elif محرف == "s":
          # apl-source:63
          قيمة = وسائط[مؤشر]
        # apl-source:64
        else:
          # apl-source:65
          قيمة = سداسي_نص(وسائط[مؤشر])
        # apl-source:66
        مؤشر = مؤشر + 1
        # apl-source:67
        while len(قيمة) < عرض:
          # apl-source:68
          قيمة = حشو + قيمة
        # apl-source:69
        ناتج = ناتج + قيمة
        # apl-source:70
        ي = ي + 1
    # apl-source:71
    else:
      # apl-source:72
      ناتج = ناتج + قالب[ي]
      # apl-source:73
      ي = ي + 1
  # apl-source:74
  return ناتج
# apl-source:75

# apl-source:76
تأكد_يساوي(تنسيق("%d + %d = %d", [2, 3, 5]), "2 + 3 = 5", "جمع بسيط")
# apl-source:77
تأكد_يساوي(تنسيق("hex: %x", [255]), "hex: ff", "سداسي")
# apl-source:78
تأكد_يساوي(تنسيق("[%05d]", [42]), "[00042]", "حشو أصفار")
# apl-source:79
تأكد_يساوي(تنسيق("%s=%d", ["x", 7]), "x=7", "نص ورقم")
# apl-source:80
تأكد_يساوي(تنسيق("100%%", []), "100%", "علامة مئوية مهربة")
# apl-source:81
تأكد_يساوي(سداسي_نص(0), "0", "صفر سداسي")
# apl-source:82
