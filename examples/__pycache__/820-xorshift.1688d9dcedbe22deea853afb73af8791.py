
# apl-source:1
# مثال 820 — مولد xorshift
# apl-source:2
# xorshift PRNG
# apl-source:3
# Demonstrates: ثلاث إزاحات XOR، دورة قصوى
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/820-xorshift.apl
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
# مولد xorshift32: ثلاث إزاحات مع حصر ثنائي فقط
# apl-source:25
# Demonstrates: إزاحة وXOR, دورة 2^32-1, سرعة بدون ضرب
# apl-source:26

# apl-source:27
قناع = 4294967295
# apl-source:28

# apl-source:29
def خطوة_شيفت(س):
  # apl-source:30
  س = س ^ ((س << 13) & قناع)
  # apl-source:31
  س = س ^ (س >> 17)
  # apl-source:32
  س = س ^ ((س << 5) & قناع)
  # apl-source:33
  return س
# apl-source:34

# apl-source:35
س = 1
# apl-source:36
تأكد_يساوي(خطوة_شيفت(س), 270369, "أول قيمة")
# apl-source:37
سلسلة = []
# apl-source:38
for ي in range(3):
  # apl-source:39
  س = خطوة_شيفت(س)
  # apl-source:40
  سلسلة.append(س)
# apl-source:41
تأكد_يساوي(سلسلة, [270369, 67634689, 2647435461], "ثلاث قيم")
# apl-source:42
تأكد_يساوي(خطوة_شيفت(0), 0, "الصفر حالة ميتة")
# apl-source:43
بايتات = []
# apl-source:44
س = 2463534242
# apl-source:45
for ي in range(4):
  # apl-source:46
  س = خطوة_شيفت(س)
  # apl-source:47
  بايتات.append(س % 256)
# apl-source:48
تأكد_يساوي(بايتات, [99, 122, 160, 126], "بايتات من بذرة أخرى")
# apl-source:49
