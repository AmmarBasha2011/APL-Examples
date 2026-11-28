
# apl-source:1
# مثال 821 — مولد SplitMix64
# apl-source:2
# SplitMix64
# apl-source:3
# Demonstrates: عداد ذهبي، خلط ستافورد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/821-splitmix.apl
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
# مولد SplitMix64: عداد ذهبي مع خلط ستافورد 13
# apl-source:25
# Demonstrates: ثابت النسبة الذهبية, خلط بإزاحات وضرب, حالة 64-بت
# apl-source:26

# apl-source:27
م64 = 18446744073709551616
# apl-source:28

# apl-source:29
def خطوة_سبليت(س):
  # apl-source:30
  س = (س + 11400714819323198485) % م64
  # apl-source:31
  ز = س
  # apl-source:32
  ز = ((ز ^ (ز >> 30)) * 13787848793156543929) % م64
  # apl-source:33
  ز = ((ز ^ (ز >> 27)) * 10723151780598845931) % م64
  # apl-source:34
  ز = ز ^ (ز >> 31)
  # apl-source:35
  return [س, ز]
# apl-source:36

# apl-source:37
حالة = 12345
# apl-source:38
نتيجة = خطوة_سبليت(حالة)
# apl-source:39
تأكد_يساوي(نتيجة[1], 2454886589211414944, "أول قيمة")
# apl-source:40
حالة = نتيجة[0]
# apl-source:41
نتيجة = خطوة_سبليت(حالة)
# apl-source:42
تأكد_يساوي(نتيجة[1], 3778200017661327597, "ثاني قيمة")
# apl-source:43
حالة = نتيجة[0]
# apl-source:44
نتيجة = خطوة_سبليت(حالة)
# apl-source:45
تأكد_يساوي(نتيجة[1], 2205171434679333405, "ثالث قيمة")
# apl-source:46
تأكد_يساوي(2454886589211414944 != 3778200017661327597 == False, False, "قيم متمايزة")
# apl-source:47
