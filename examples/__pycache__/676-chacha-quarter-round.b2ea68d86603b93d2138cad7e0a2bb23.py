
# apl-source:1
# مثال 676 — ربع دورة تشاتشا
# apl-source:2
# ChaCha quarter round
# apl-source:3
# Demonstrates: دوران بتات، جمع معياري، XOR
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/676-chacha-quarter-round.apl
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
# ربع دورة تشاتشا
# apl-source:25
# Demonstrates: جمع معياري 32 بت, تدوير بتات, خلط ARX
# apl-source:26
# اللبنة التي يبنى منها تشفير ChaCha20 كله
# apl-source:27

# apl-source:28
قناع = 4294967295
# apl-source:29

# apl-source:30
def دوّر(س, ك):
  # apl-source:31
  return ((س << ك) & قناع) | (س >> (32 - ك))
# apl-source:32

# apl-source:33
def ربع_دورة(أ, ب, ج, د):
  # apl-source:34
  أ = (أ + ب) & قناع
  # apl-source:35
  د = دوّر(د ^ أ, 16)
  # apl-source:36
  ج = (ج + د) & قناع
  # apl-source:37
  ب = دوّر(ب ^ ج, 12)
  # apl-source:38
  أ = (أ + ب) & قناع
  # apl-source:39
  د = دوّر(د ^ أ, 8)
  # apl-source:40
  ج = (ج + د) & قناع
  # apl-source:41
  ب = دوّر(ب ^ ج, 7)
  # apl-source:42
  return [أ, ب, ج, د]
# apl-source:43

# apl-source:44
نتيجة = ربع_دورة(0x11111111, 0x01020304, 0x9b8d6f43, 0x01234567)
# apl-source:45
تأكد_يساوي(نتيجة, [0xea2a92f4, 0xcb1cf8ce, 0x4581472e, 0x5881c4bb], "متجه RFC")
# apl-source:46
صفر = ربع_دورة(0, 0, 0, 0)
# apl-source:47
تأكد_يساوي(صفر, [0, 0, 0, 0], "الأصفار تبقى أصفارا")
# apl-source:48
تأكد_يساوي(نتيجة[0] <= قناع, True, "ضمن 32 بت")
# apl-source:49
print("النتيجة:", نتيجة)
# apl-source:50
