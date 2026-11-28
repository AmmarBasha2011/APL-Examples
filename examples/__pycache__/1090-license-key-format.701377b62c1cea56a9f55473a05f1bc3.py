
# apl-source:1
# مثال 1090 — تنسيق مفتاح الترخيص
# apl-source:2
# License key formatting
# apl-source:3
# Demonstrates: تجميع من النهاية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1090-license-key-format.apl
# apl-source:6

# apl-source:7
# نحذف الشرطات ونحول الحروف لكبيرة
# apl-source:8
# ثم نجمع من النهاية بمجموعات طولها ك والأولى قد تكون أقصر
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
def كبيرة(ح):
  # apl-source:19
  صغيرة = "abcdefghijklmnopqrstuvwxyz"
  # apl-source:20
  كبيرة_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  # apl-source:21
  for ع in range(26):
    # apl-source:22
    if صغيرة[ع] == ح:
      # apl-source:23
      return كبيرة_[ع]
  # apl-source:24
  return ح
# apl-source:25

# apl-source:26
def نسّق(مفتاح, ك):
  # apl-source:27
  نظيف = ""
  # apl-source:28
  for ح in مفتاح:
    # apl-source:29
    if ح != "-":
      # apl-source:30
      نظيف = نظيف + كبيرة(ح)
  # apl-source:31
  اجزاء = []
  # apl-source:32
  ن = len(نظيف)
  # apl-source:33
  اول = ن % ك
  # apl-source:34
  if اول > 0:
    # apl-source:35
    اجزاء = اجزاء + [نظيف[:اول]]
  # apl-source:36
  for ع in range(اول, ن, ك):
    # apl-source:37
    اجزاء = اجزاء + [نظيف[ع:ع + ك]]
  # apl-source:38
  return "-".join(اجزاء)
# apl-source:39

# apl-source:40
تأكد_يساوي(نسّق("5F3Z-2e-9-w", 4), "5F3Z-2E9W", "مجموعات أربع")
# apl-source:41
تأكد_يساوي(نسّق("2-5g-3-J", 2), "2-5G-3J", "مجموعات اثنتان")
# apl-source:42
تأكد_يساوي(نسّق("---", 2), "", "شرطات فقط")
# apl-source:43
