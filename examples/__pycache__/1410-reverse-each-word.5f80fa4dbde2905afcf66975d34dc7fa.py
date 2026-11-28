
# apl-source:1
# مثال 1410 — عكس كل كلمة
# apl-source:2
# Reverse each word in sentence
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1410-reverse-each-word.apl
# apl-source:6

# apl-source:7
# نقسم الجملة عند المسافات
# apl-source:8
# نعكس كل كلمة ونعيد جمعها
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def اعكس_كلمة(ك):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  for ح in ك:
    # apl-source:21
    ناتج = ح + ناتج
  # apl-source:22
  return ناتج
# apl-source:23

# apl-source:24
def اعكس_الكلمات(جملة):
  # apl-source:25
  كلمات = جملة.split(" ")
  # apl-source:26
  ناتج = ""
  # apl-source:27
  for ع in range(len(كلمات)):
    # apl-source:28
    if ع > 0:
      # apl-source:29
      ناتج = ناتج + " "
    # apl-source:30
    ناتج = ناتج + اعكس_كلمة(كلمات[ع])
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
تأكد_يساوي(اعكس_الكلمات("God Ding"), "doG gniD", "كلمتان")
# apl-source:34
تأكد_يساوي(اعكس_الكلمات("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc", "جملة")
# apl-source:35
تأكد_يساوي(اعكس_الكلمات("a"), "a", "حرف")
# apl-source:36
