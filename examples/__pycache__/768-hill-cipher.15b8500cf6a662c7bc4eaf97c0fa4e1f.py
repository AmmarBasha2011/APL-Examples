
# apl-source:1
# مثال 768 — شفرة هيل
# apl-source:2
# Hill cipher
# apl-source:3
# Demonstrates: مصفوفة مفتاح، معكوس مودولو 26
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/768-hill-cipher.apl
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
# شفرة هيل: ضرب مصفوفة 2×2 بأزواج الحروف مودولو 26
# apl-source:25
# Demonstrates: مصفوفة مفتاح, دترمننت ومعكوس مصفوفة مودولو 26
# apl-source:26

# apl-source:27
def عاكس_ضربي(أ):
  # apl-source:28
  for ي in range(1, 26):
    # apl-source:29
    if (أ * ي) % 26 == 1:
      # apl-source:30
      return ي
  # apl-source:31
  return 0
# apl-source:32

# apl-source:33
def هيل_تشفير(نص, ك):
  # apl-source:34
  ناتج = ""
  # apl-source:35
  for ي in range(len(نص) // 2):
    # apl-source:36
    س = ord(نص[ي * 2]) - 65
    # apl-source:37
    ص = ord(نص[ي * 2 + 1]) - 65
    # apl-source:38
    ناتج = ناتج + chr((ك[0][0] * س + ك[0][1] * ص) % 26 + 65)
    # apl-source:39
    ناتج = ناتج + chr((ك[1][0] * س + ك[1][1] * ص) % 26 + 65)
  # apl-source:40
  return ناتج
# apl-source:41

# apl-source:42
def هيل_فك(نص, ك):
  # apl-source:43
  دترمننت = (ك[0][0] * ك[1][1] - ك[0][1] * ك[1][0]) % 26
  # apl-source:44
  عاكس = عاكس_ضربي(دترمننت)
  # apl-source:45
  كع = [[(ك[1][1] * عاكس) % 26, ((0 - ك[0][1]) * عاكس) % 26], [((0 - ك[1][0]) * عاكس) % 26, (ك[0][0] * عاكس) % 26]]
  # apl-source:46
  return هيل_تشفير(نص, كع)
# apl-source:47

# apl-source:48
ك = [[3, 3], [2, 5]]
# apl-source:49
تأكد_يساوي(هيل_تشفير("HELP", ك), "HIAT", "متجه ويكيبيديا هيل")
# apl-source:50
تأكد_يساوي(هيل_تشفير("HELLOWORLD", ك), "HIOZEIPJQL", "هيل لكلمة أطول")
# apl-source:51
تأكد_يساوي(هيل_فك("HIOZEIPJQL", ك), "HELLOWORLD", "فك هيل")
# apl-source:52
تأكد_يساوي(هيل_فك(هيل_تشفير("MATRICES", ك), ك), "MATRICES", "ذهاب وإياب")
# apl-source:53
