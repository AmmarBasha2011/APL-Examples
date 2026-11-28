
# apl-source:1
# مثال 1092 — عناوين البريد الفريدة
# apl-source:2
# Unique email addresses
# apl-source:3
# Demonstrates: تطبيع الجزء المحلي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1092-unique-emails.apl
# apl-source:6

# apl-source:7
# الجزء المحلي يتجاهل النقاط وكل ما بعد علامة الزائد
# apl-source:8
# النطاق يبقى كما هو ثم نعد العناوين المختلفة
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
def طبّع(عنوان):
  # apl-source:19
  محلي = ""
  # apl-source:20
  for ع in range(len(عنوان)):
    # apl-source:21
    if عنوان[ع] == "@":
      # apl-source:22
      return محلي + عنوان[ع:]
    # apl-source:23
    if عنوان[ع] == "+":
      # apl-source:24
      ك = ع
      # apl-source:25
      while عنوان[ك] != "@":
        # apl-source:26
        ك = ك + 1
      # apl-source:27
      return محلي + عنوان[ك:]
    # apl-source:28
    if عنوان[ع] != ".":
      # apl-source:29
      محلي = محلي + عنوان[ع]
  # apl-source:30
  return محلي
# apl-source:31

# apl-source:32
def عدد_فريد(عناوين):
  # apl-source:33
  رأيت = []
  # apl-source:34
  for ع in عناوين:
    # apl-source:35
    ن = طبّع(ع)
    # apl-source:36
    if ن not in رأيت:
      # apl-source:37
      رأيت = رأيت + [ن]
  # apl-source:38
  return len(رأيت)
# apl-source:39

# apl-source:40
تأكد_يساوي(طبّع("test.email+alex@leetcode.com"), "testemail@leetcode.com", "نقطة وزائد")
# apl-source:41
تأكد_يساوي(عدد_فريد(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]), 2, "اثنان")
# apl-source:42
تأكد_يساوي(عدد_فريد(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]), 3, "ثلاثة")
# apl-source:43
