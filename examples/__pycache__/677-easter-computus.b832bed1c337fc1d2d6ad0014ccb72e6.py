
# apl-source:1
# مثال 677 — حساب عيد الفصح
# apl-source:2
# Easter computus
# apl-source:3
# Demonstrates: حساب فلكي، تاريخ قمري شمسي، معادلات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/677-easter-computus.apl
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
# حساب عيد الفصح الغربي
# apl-source:25
# Demonstrates: خوارزمية كمبوتوس, باقيات متتالية, قمر كنسي
# apl-source:26
# يحدد تاريخا قمريا شمسيا بلا جداول
# apl-source:27

# apl-source:28
def فصح(سنة):
  # apl-source:29
  أ = سنة % 19
  # apl-source:30
  ب = سنة // 100
  # apl-source:31
  ج = سنة % 100
  # apl-source:32
  د = ب // 4
  # apl-source:33
  ه = ب % 4
  # apl-source:34
  ف = (ب + 8) // 25
  # apl-source:35
  ز = (ب - ف + 1) // 3
  # apl-source:36
  ح = (19 * أ + ب - د - ز + 15) % 30
  # apl-source:37
  ط = ج // 4
  # apl-source:38
  ك = ج % 4
  # apl-source:39
  ل = (32 + 2 * ه + 2 * ط - ح - ك) % 7
  # apl-source:40
  م = (أ + 11 * ح + 22 * ل) // 451
  # apl-source:41
  شهر = (ح + ل - 7 * م + 114) // 31
  # apl-source:42
  يوم = (ح + ل - 7 * م + 114) % 31 + 1
  # apl-source:43
  return [شهر, يوم]
# apl-source:44

# apl-source:45
تأكد_يساوي(فصح(2000), [4, 23], "فصح 2000")
# apl-source:46
تأكد_يساوي(فصح(2023), [4, 9], "فصح 2023")
# apl-source:47
تأكد_يساوي(فصح(2024), [3, 31], "فصح 2024")
# apl-source:48
تأكد_يساوي(فصح(2025), [4, 20], "فصح 2025")
# apl-source:49
تأكد_يساوي(فصح(2026), [4, 5], "فصح 2026")
# apl-source:50
تأكد_يساوي(فصح(1900), [4, 15], "فصح 1900")
# apl-source:51
print("فصح 2026:", فصح(2026))
# apl-source:52
