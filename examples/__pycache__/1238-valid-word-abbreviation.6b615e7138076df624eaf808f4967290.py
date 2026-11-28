
# apl-source:1
# مثال 1238 — اختصار كلمة صالح
# apl-source:2
# Valid word abbreviation
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1238-valid-word-abbreviation.apl
# apl-source:6

# apl-source:7
# الأرقام تعني عدد الحروف المتجاوزة
# apl-source:8
# ولا يبدأ الرقم بصفر
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
def صالح(كلمة, اختصار):
  # apl-source:19
  ك = 0
  # apl-source:20
  ا = 0
  # apl-source:21
  while (ك < len(كلمة)) and (ا < len(اختصار)):
    # apl-source:22
    if اختصار[ا].isdigit():
      # apl-source:23
      if اختصار[ا] == "0":
        # apl-source:24
        return False
      # apl-source:25
      ن = 0
      # apl-source:26
      while (ا < len(اختصار)) and اختصار[ا].isdigit():
        # apl-source:27
        ن = ن * 10 + int(اختصار[ا])
        # apl-source:28
        ا = ا + 1
      # apl-source:29
      ك = ك + ن
    # apl-source:30
    else:
      # apl-source:31
      if كلمة[ك] != اختصار[ا]:
        # apl-source:32
        return False
      # apl-source:33
      ك = ك + 1
      # apl-source:34
      ا = ا + 1
  # apl-source:35
  return (ك == len(كلمة)) and (ا == len(اختصار))
# apl-source:36

# apl-source:37
تأكد_يساوي(صالح("internationalization", "i12iz4n"), True, "صالح")
# apl-source:38
تأكد_يساوي(صالح("apple", "a2e"), False, "حرف خاطئ")
# apl-source:39
تأكد_يساوي(صالح("substitution", "s10n"), True, "عشرة")
# apl-source:40
تأكد_يساوي(صالح("hi", "01"), False, "صفر بادئ")
# apl-source:41
