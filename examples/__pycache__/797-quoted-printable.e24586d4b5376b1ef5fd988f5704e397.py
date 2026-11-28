
# apl-source:1
# مثال 797 — Quoted-Printable
# apl-source:2
# Quoted-Printable
# apl-source:3
# Demonstrates: تهريب =XX، فك عكسي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/797-quoted-printable.apl
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
# ترميز Quoted-Printable للبريد: ASCII يمر وغيره يصبح =XX
# apl-source:25
# Demonstrates: فحص مجال البايتات, تهريب سداسي عشري, فك عكسي
# apl-source:26

# apl-source:27
سداسي = "0123456789ABCDEF"
# apl-source:28

# apl-source:29
def ترميز_qp(نص):
  # apl-source:30
  ناتج = ""
  # apl-source:31
  for ح in نص:
    # apl-source:32
    ك = ord(ح)
    # apl-source:33
    if (ك >= 33 and ك <= 60) or (ك >= 62 and ك <= 126):
      # apl-source:34
      ناتج = ناتج + ح
    # apl-source:35
    else:
      # apl-source:36
      if ك == 32:
        # apl-source:37
        ناتج = ناتج + " "
      # apl-source:38
      else:
        # apl-source:39
        ناتج = ناتج + "=" + سداسي[ك // 16] + سداسي[ك % 16]
  # apl-source:40
  return ناتج
# apl-source:41

# apl-source:42
def قيمة_سداسي(ح):
  # apl-source:43
  for ي in range(16):
    # apl-source:44
    if سداسي[ي] == ح:
      # apl-source:45
      return ي
  # apl-source:46
  return 0
# apl-source:47

# apl-source:48
def فك_qp(مشفر):
  # apl-source:49
  ناتج = ""
  # apl-source:50
  ي = 0
  # apl-source:51
  while ي < len(مشفر):
    # apl-source:52
    if مشفر[ي] == "=":
      # apl-source:53
      ناتج = ناتج + chr(قيمة_سداسي(مشفر[ي + 1]) * 16 + قيمة_سداسي(مشفر[ي + 2]))
      # apl-source:54
      ي = ي + 3
    # apl-source:55
    else:
      # apl-source:56
      ناتج = ناتج + مشفر[ي]
      # apl-source:57
      ي = ي + 1
  # apl-source:58
  return ناتج
# apl-source:59

# apl-source:60
تأكد_يساوي(ترميز_qp("Hello World"), "Hello World", "نص عادي يمر")
# apl-source:61
تأكد_يساوي(ترميز_qp("a=b"), "a=3Db", "علامة يساوي تهرب")
# apl-source:62
تأكد_يساوي(ترميز_qp("tab	here"), "tab=09here", "تاب يهرب")
# apl-source:63
تأكد_يساوي(فك_qp("Hello=20World=3Dok"), "Hello World=ok", "فك التهريب")
# apl-source:64
تأكد_يساوي(فك_qp(ترميز_qp("price=100%")), "price=100%", "دورة كاملة")
# apl-source:65
