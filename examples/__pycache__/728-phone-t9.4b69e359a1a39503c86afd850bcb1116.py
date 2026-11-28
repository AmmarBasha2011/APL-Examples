
# apl-source:1
# مثال 728 — لوحة T9
# apl-source:2
# Phone T9 keypad
# apl-source:3
# Demonstrates: خريطة أرقام، ضغطات، تتابع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/728-phone-t9.apl
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
# لوحة T9 القديمة: حروف إلى أرقام وتخمين كلمات
# apl-source:25
# Demonstrates: خريطة حرف-رقم, بحث عكسي بقاموس, كلمات متجانية رقميا
# apl-source:26
# 4663 تعني home و good و gone معا
# apl-source:27

# apl-source:28
def رقم_t9(ح):
  # apl-source:29
  if ح in "abc":
    # apl-source:30
    return "2"
  # apl-source:31
  if ح in "def":
    # apl-source:32
    return "3"
  # apl-source:33
  if ح in "ghi":
    # apl-source:34
    return "4"
  # apl-source:35
  if ح in "jkl":
    # apl-source:36
    return "5"
  # apl-source:37
  if ح in "mno":
    # apl-source:38
    return "6"
  # apl-source:39
  if ح in "pqrs":
    # apl-source:40
    return "7"
  # apl-source:41
  if ح in "tuv":
    # apl-source:42
    return "8"
  # apl-source:43
  if ح in "wxyz":
    # apl-source:44
    return "9"
  # apl-source:45
  return "0"
# apl-source:46

# apl-source:47
def إلى_أرقام(كلمة):
  # apl-source:48
  ناتج = ""
  # apl-source:49
  for ي in range(len(كلمة)):
    # apl-source:50
    ناتج = ناتج + رقم_t9(كلمة[ي])
  # apl-source:51
  return ناتج
# apl-source:52

# apl-source:53
def تخمين(أرقام, قاموس):
  # apl-source:54
  ناتج = []
  # apl-source:55
  for ك in قاموس:
    # apl-source:56
    if إلى_أرقام(ك) == أرقام:
      # apl-source:57
      ناتج.append(ك)
  # apl-source:58
  return ناتج
# apl-source:59

# apl-source:60
تأكد_يساوي(إلى_أرقام("hello"), "43556", "مرحبا")
# apl-source:61
تأكد_يساوي(إلى_أرقام("world"), "96753", "عالم")
# apl-source:62
تأكد_يساوي(إلى_أرقام("home"), "4663", "منزل")
# apl-source:63
قاموس = ["home", "good", "gone", "hood", "hoof", "inn", "cat", "act", "bat"]
# apl-source:64
ت = تخمين("4663", قاموس)
# apl-source:65
تأكد_يساوي("home" in ت, True, "home ضمن التخمينات")
# apl-source:66
تأكد_يساوي("good" in ت, True, "good ضمن التخمينات")
# apl-source:67
تأكد_يساوي("gone" in ت, True, "gone ضمن التخمينات")
# apl-source:68
تأكد_يساوي("cat" in ت, False, "cat ليست 4663")
# apl-source:69
ت2 = تخمين("228", قاموس)
# apl-source:70
تأكد_يساوي("cat" in ت2 and "act" in ت2 and "bat" in ت2, True, "228 ثلاث كلمات")
# apl-source:71
تأكد_يساوي(len(تخمين("9999", قاموس)), 0, "لا تطابق")
# apl-source:72
print("4663:", ت)
# apl-source:73
