
# apl-source:1
# مثال 1983 — توحيد صيغة عنوان MAC
# apl-source:2
# MAC address normalize
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1983-mac-address-normalize-format.apl
# apl-source:6

# apl-source:7
# # نحذف الشرطة والنقطتين والنقطة
# apl-source:8
# # ثم نقسم كل حرفين
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
def وحد(س):
  # apl-source:19
  نظيف = ""
  # apl-source:20
  for ح in س:
    # apl-source:21
    if (ح in "-:.") == False:
      # apl-source:22
      نظيف = نظيف + ح.lower()
  # apl-source:23
  اجزاء = []
  # apl-source:24
  for ك in range(0, len(نظيف), 2):
    # apl-source:25
    اجزاء = اجزاء + [نظيف[ك:ك + 2]]
  # apl-source:26
  return ":".join(اجزاء)
# apl-source:27

# apl-source:28
تأكد_يساوي(وحد("AA-BB-CC-DD-EE-FF"), "aa:bb:cc:dd:ee:ff", "شرطات")
# apl-source:29
تأكد_يساوي(وحد("aabb.ccdd.eeff"), "aa:bb:cc:dd:ee:ff", "نقاط")
# apl-source:30
تأكد_يساوي(وحد("01:23:45:67:89:AB"), "01:23:45:67:89:ab", "نقطتان")
# apl-source:31
