
# apl-source:1
# مثال 1978 — التحقق من صيغة عنوان IPv4
# apl-source:2
# IPv4 format validation
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1978-ipv4-address-format-validate.apl
# apl-source:6

# apl-source:7
# # نقسم عند النقطة ونفحص كل جزء
# apl-source:8
# # الجزء 0 وحده يقبل بصفر
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
def صالح(س):
  # apl-source:19
  اجزاء = س.split(".")
  # apl-source:20
  if len(اجزاء) != 4:
    # apl-source:21
    return False
  # apl-source:22
  for ج in اجزاء:
    # apl-source:23
    if ج == "" or (ج.isdigit() == False):
      # apl-source:24
      return False
    # apl-source:25
    if len(ج) > 1 and ج[0] == "0":
      # apl-source:26
      return False
    # apl-source:27
    if int(ج) > 255:
      # apl-source:28
      return False
  # apl-source:29
  return True
# apl-source:30

# apl-source:31
تأكد_يساوي(صالح("192.168.1.1"), True, "صحيح")
# apl-source:32
تأكد_يساوي(صالح("256.1.1.1"), False, "كبير")
# apl-source:33
تأكد_يساوي(صالح("1.2.3"), False, "ثلاثة أجزاء")
# apl-source:34
تأكد_يساوي(صالح("01.2.3.4"), False, "صفر بادئ")
# apl-source:35
تأكد_يساوي(صالح("a.b.c.d"), False, "حروف")
# apl-source:36
تأكد_يساوي(صالح("0.0.0.0"), True, "أصفار")
# apl-source:37
