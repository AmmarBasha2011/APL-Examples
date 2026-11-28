
# apl-source:1
# مثال 1979 — تحويل IPv4 إلى عدد صحيح والعكس
# apl-source:2
# IPv4 to integer and back
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1979-ipv4-to-integer-and-back.apl
# apl-source:6

# apl-source:7
# # نضرب الناتج في 256 ونضيف كل جزء
# apl-source:8
# # وللعكس نأخذ الباقي على 256 من اليمين
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
def الى_عدد(س):
  # apl-source:19
  ن = 0
  # apl-source:20
  for ج in س.split("."):
    # apl-source:21
    ن = ن * 256 + int(ج)
  # apl-source:22
  return ن
# apl-source:23

# apl-source:24
def الى_عنوان(ن):
  # apl-source:25
  اجزاء = []
  # apl-source:26
  for ك in range(4):
    # apl-source:27
    اجزاء = [str(ن % 256)] + اجزاء
    # apl-source:28
    ن = ن // 256
  # apl-source:29
  return ".".join(اجزاء)
# apl-source:30

# apl-source:31
تأكد_يساوي(الى_عدد("192.168.1.1"), 3232235777, "عادي")
# apl-source:32
تأكد_يساوي(الى_عدد("0.0.0.0"), 0, "أصفار")
# apl-source:33
تأكد_يساوي(الى_عدد("255.255.255.255"), 4294967295, "أقصى")
# apl-source:34
تأكد_يساوي(الى_عنوان(3232235777), "192.168.1.1", "عكس")
# apl-source:35
