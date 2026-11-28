
# apl-source:1
# مثال 1427 — تشابه الجمل
# apl-source:2
# Sentence similarity with pairs
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1427-sentence-similarity-pairs.apl
# apl-source:6

# apl-source:7
# الجملتان بنفس الطول
# apl-source:8
# كل كلمتين متقابلتين متساويتان أو زوج متشابه
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
def متشابهتان(أ, ب, ازواج):
  # apl-source:19
  if len(أ) != len(ب):
    # apl-source:20
    return False
  # apl-source:21
  مشابه = {}
  # apl-source:22
  for ز in ازواج:
    # apl-source:23
    مشابه[ز[0] + "|" + ز[1]] = True
    # apl-source:24
    مشابه[ز[1] + "|" + ز[0]] = True
  # apl-source:25
  for ع in range(len(أ)):
    # apl-source:26
    if أ[ع] != ب[ع]:
      # apl-source:27
      if not مشابه.get(أ[ع] + "|" + ب[ع], False):
        # apl-source:28
        return False
  # apl-source:29
  return True
# apl-source:30

# apl-source:31
ز = [["great","fine"],["drama","acting"],["skills","talent"]]
# apl-source:32
تأكد_يساوي(متشابهتان(["great","acting","skills"], ["fine","drama","talent"], ز), True, "متشابهتان")
# apl-source:33
تأكد_يساوي(متشابهتان(["great"], ["great"], []), True, "نفس الكلمة")
# apl-source:34
تأكد_يساوي(متشابهتان(["great"], ["double"], ز), False, "مختلفتان")
# apl-source:35
