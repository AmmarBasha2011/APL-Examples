
# apl-source:1
# مثال 1913 — لعبة البطاطا الساخنة
# apl-source:2
# Hot potato game last player
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1913-hot-potato-queue-last-player.apl
# apl-source:6

# apl-source:7
# نمرر البطاطا عددا ثابتا من المرات
# apl-source:8
# اللاعب الذي معه البطاطا يخرج
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
def بطاطا(اسماء, مرات):
  # apl-source:19
  طابور = اسماء + []
  # apl-source:20
  while len(طابور) > 1:
    # apl-source:21
    for ك in range(مرات):
      # apl-source:22
      أول = طابور.pop(0)
      # apl-source:23
      طابور = طابور + [أول]
    # apl-source:24
    طابور.pop(0)
  # apl-source:25
  return طابور[0]
# apl-source:26

# apl-source:27
تأكد_يساوي(بطاطا(["a", "b", "c", "d"], 2), "a", "أربعة لاعبين")
# apl-source:28
تأكد_يساوي(بطاطا(["x"], 5), "x", "لاعب واحد")
# apl-source:29
تأكد_يساوي(بطاطا(["a", "b", "c"], 1), "c", "مرة واحدة")
# apl-source:30
