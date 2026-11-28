
# apl-source:1
# مثال 1494 — عنوان IPv4 صحيح
# apl-source:2
# Validate IPv4 address
# apl-source:3
# Demonstrates: تحليل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1494-ipv4-address-valid.apl
# apl-source:6

# apl-source:7
# نفصل على النقاط
# apl-source:8
# نرفض الجزء الفارغ والأصفار البادئة
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
def عنوان_صحيح(نص_):
  # apl-source:19
  أجزاء = نص_.split(".")
  # apl-source:20
  if len(أجزاء) != 4:
    # apl-source:21
    return False
  # apl-source:22
  for ج in أجزاء:
    # apl-source:23
    if ج == "" or ج.isdigit() == False:
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
تأكد_يساوي(عنوان_صحيح("192.168.1.1"), True, "صحيح")
# apl-source:32
تأكد_يساوي(عنوان_صحيح("256.1.1.1"), False, "كبير")
# apl-source:33
تأكد_يساوي(عنوان_صحيح("1.2.3"), False, "ناقص")
# apl-source:34
تأكد_يساوي(عنوان_صحيح("01.2.3.4"), False, "صفر بادئ")
# apl-source:35
