
# apl-source:1
# مثال 800 — تفريغ سداسي
# apl-source:2
# Hex dump
# apl-source:3
# Demonstrates: إزاحة، أعمدة، ASCII
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/800-hex-dump.apl
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
# تفريغ سداسي عشري بأسلوب hexdump: إزاحة وبايتات وحرف ASCII
# apl-source:25
# Demonstrates: تنسيق بخانة سداسية ثابتة, محاذاة الأعمدة, نقطة للمحرف غير القابل للطباعة
# apl-source:26

# apl-source:27
سداسي = "0123456789abcdef"
# apl-source:28

# apl-source:29
def سداسي2(ب):
  # apl-source:30
  return سداسي[ب // 16] + سداسي[ب % 16]
# apl-source:31

# apl-source:32
def سداسي4(ن):
  # apl-source:33
  return سداسي2(ن // 256) + سداسي2(ن % 256)
# apl-source:34

# apl-source:35
def كرر(نص, عدد):
  # apl-source:36
  ناتج = ""
  # apl-source:37
  for ي in range(عدد):
    # apl-source:38
    ناتج = ناتج + نص
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
def تفريغ(بيانات, عرض):
  # apl-source:42
  ب = []
  # apl-source:43
  for حرف in بيانات:
    # apl-source:44
    ب.append(ord(حرف))
  # apl-source:45
  أسطر = []
  # apl-source:46
  ي = 0
  # apl-source:47
  while ي < len(ب):
    # apl-source:48
    قطعة = []
    # apl-source:49
    نص = ""
    # apl-source:50
    for ك in range(عرض):
      # apl-source:51
      if ي + ك < len(ب):
        # apl-source:52
        قطعة.append(سداسي2(ب[ي + ك]))
        # apl-source:53
        كود = ب[ي + ك]
        # apl-source:54
        if كود >= 32 and كود < 127:
          # apl-source:55
          نص = نص + chr(كود)
        # apl-source:56
        else:
          # apl-source:57
          نص = نص + "."
    # apl-source:58
    سطر = سداسي4(ي) + "  " + " ".join(قطعة)
    # apl-source:59
    نقص = عرض - len(قطعة)
    # apl-source:60
    سطر = سطر + كرر("   ", نقص) + "  |" + نص + "|"
    # apl-source:61
    أسطر.append(سطر)
    # apl-source:62
    ي = ي + عرض
  # apl-source:63
  return أسطر
# apl-source:64

# apl-source:65
نتيجة = تفريغ("Hello, World!", 8)
# apl-source:66
تأكد_يساوي(نتيجة[0], "0000  48 65 6c 6c 6f 2c 20 57  |Hello, W|", "السطر الأول")
# apl-source:67
تأكد_يساوي(نتيجة[1], "0008  6f 72 6c 64 21           |orld!|", "سطر غير مكتمل")
# apl-source:68
تأكد_يساوي(سداسي2(255), "ff", "أعلى بايت")
# apl-source:69
تأكد_يساوي(سداسي4(30), "001e", "إزاحة من أربع خانات")
# apl-source:70
تأكد_يساوي(len(تفريغ("ABCDEFGHIJKLMNOP", 16)), 1, "سطر واحد كامل")
# apl-source:71
