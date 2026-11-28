
# apl-source:1
# مثال 1495 — عنوان MAC صحيح
# apl-source:2
# Validate MAC address
# apl-source:3
# Demonstrates: تحليل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1495-mac-address-valid.apl
# apl-source:6

# apl-source:7
# نفصل على النقطتين
# apl-source:8
# كل جزء حرفان من الأرقام السداسية العشرية
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
def ماك_صحيح(نص_):
  # apl-source:19
  أجزاء = نص_.split(":")
  # apl-source:20
  if len(أجزاء) != 6:
    # apl-source:21
    return False
  # apl-source:22
  مسموح = "0123456789abcdefABCDEF"
  # apl-source:23
  for ج in أجزاء:
    # apl-source:24
    if len(ج) != 2:
      # apl-source:25
      return False
    # apl-source:26
    for ح in ج:
      # apl-source:27
      موجود = ح in مسموح
      # apl-source:28
      if موجود == False:
        # apl-source:29
        return False
  # apl-source:30
  return True
# apl-source:31

# apl-source:32
تأكد_يساوي(ماك_صحيح("00:1A:2b:3C:4d:5E"), True, "صحيح")
# apl-source:33
تأكد_يساوي(ماك_صحيح("00:1A:2b:3C:4d"), False, "ناقص")
# apl-source:34
تأكد_يساوي(ماك_صحيح("00:1A:2b:3C:4d:5G"), False, "حرف خاطئ")
# apl-source:35
