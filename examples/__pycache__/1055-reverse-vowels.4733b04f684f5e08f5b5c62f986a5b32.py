
# apl-source:1
# مثال 1055 — عكس الحروف المتحركة
# apl-source:2
# Reverse vowels of a string
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1055-reverse-vowels.apl
# apl-source:6

# apl-source:7
# مؤشر من كل طرف يتخطى الحروف غير العلة
# apl-source:8
# ونبدل حرفي العلة عند التقائهما
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
def علة(ح):
  # apl-source:19
  return ح in "aeiouAEIOU"
# apl-source:20

# apl-source:21
def اعكس_علة(نص_):
  # apl-source:22
  ق = list(نص_)
  # apl-source:23
  ي = 0
  # apl-source:24
  ل = len(ق) - 1
  # apl-source:25
  while ي < ل:
    # apl-source:26
    if not علة(ق[ي]):
      # apl-source:27
      ي = ي + 1
    # apl-source:28
    elif not علة(ق[ل]):
      # apl-source:29
      ل = ل - 1
    # apl-source:30
    else:
      # apl-source:31
      مؤقت = ق[ي]
      # apl-source:32
      ق[ي] = ق[ل]
      # apl-source:33
      ق[ل] = مؤقت
      # apl-source:34
      ي = ي + 1
      # apl-source:35
      ل = ل - 1
  # apl-source:36
  return "".join(ق)
# apl-source:37

# apl-source:38
تأكد_يساوي(اعكس_علة("hello"), "holle", "hello")
# apl-source:39
تأكد_يساوي(اعكس_علة("leetcode"), "leotcede", "leetcode")
# apl-source:40
تأكد_يساوي(اعكس_علة("xyz"), "xyz", "بلا علة")
# apl-source:41
