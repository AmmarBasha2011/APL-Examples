
# apl-source:1
# مثال 1506 — تشفير أرقام الحروف
# apl-source:2
# A1Z26 letter number cipher
# apl-source:3
# Demonstrates: تشفير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1506-a1z26-cipher.apl
# apl-source:6

# apl-source:7
# a هي 1 وz هي 26
# apl-source:8
# نفصل الأرقام بشرطة
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
def الى_أرقام(نص_):
  # apl-source:19
  أبجدية = "abcdefghijklmnopqrstuvwxyz"
  # apl-source:20
  أجزاء = []
  # apl-source:21
  for ح in نص_:
    # apl-source:22
    موضع = أبجدية.find(ح)
    # apl-source:23
    if موضع >= 0:
      # apl-source:24
      أجزاء.append(str(موضع + 1))
  # apl-source:25
  return "-".join(أجزاء)
# apl-source:26

# apl-source:27
def الى_حروف(نص_):
  # apl-source:28
  أبجدية = "abcdefghijklmnopqrstuvwxyz"
  # apl-source:29
  ناتج = ""
  # apl-source:30
  for ج in نص_.split("-"):
    # apl-source:31
    ناتج = ناتج + أبجدية[int(ج) - 1]
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
تأكد_يساوي(الى_أرقام("abc"), "1-2-3", "ثلاثة")
# apl-source:35
تأكد_يساوي(الى_أرقام("zip"), "26-9-16", "كلمة")
# apl-source:36
تأكد_يساوي(الى_حروف("8-9"), "hi", "فك")
# apl-source:37
