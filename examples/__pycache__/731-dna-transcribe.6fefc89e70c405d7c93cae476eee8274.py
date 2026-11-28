
# apl-source:1
# مثال 731 — نسخ DNA
# apl-source:2
# DNA transcription
# apl-source:3
# Demonstrates: واطسون-كريك، مكمل عكسي، RNA
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/731-dna-transcribe.apl
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
# نسخ DNA إلى RNA والمكمل العكسي
# apl-source:25
# Demonstrates: خريطة قواعد, عكس سلسلة, زوج واطسون-كريك
# apl-source:26
# T تصبح U في RNA، والمكمل يقرأ بالعكس
# apl-source:27

# apl-source:28
def نسخ(سلسلة):
  # apl-source:29
  ناتج = ""
  # apl-source:30
  for ي in range(len(سلسلة)):
    # apl-source:31
    if سلسلة[ي] == "T":
      # apl-source:32
      ناتج = ناتج + "U"
    # apl-source:33
    else:
      # apl-source:34
      ناتج = ناتج + سلسلة[ي]
  # apl-source:35
  return ناتج
# apl-source:36

# apl-source:37
def مكمل(قاعدة):
  # apl-source:38
  if قاعدة == "A":
    # apl-source:39
    return "T"
  # apl-source:40
  if قاعدة == "T":
    # apl-source:41
    return "A"
  # apl-source:42
  if قاعدة == "C":
    # apl-source:43
    return "G"
  # apl-source:44
  if قاعدة == "G":
    # apl-source:45
    return "C"
  # apl-source:46
  return "N"
# apl-source:47

# apl-source:48
def مكمل_عكسي(سلسلة):
  # apl-source:49
  ناتج = ""
  # apl-source:50
  for ي in range(len(سلسلة)):
    # apl-source:51
    ناتج = ناتج + مكمل(سلسلة[len(سلسلة) - 1 - ي])
  # apl-source:52
  return ناتج
# apl-source:53

# apl-source:54
تأكد_يساوي(نسخ("ATGC"), "AUGC", "نسخ أساسي")
# apl-source:55
تأكد_يساوي(نسخ("TTTT"), "UUUU", "كل ثايمين")
# apl-source:56
تأكد_يساوي(مكمل_عكسي("ATGC"), "GCAT", "مكمل عكسي")
# apl-source:57
تأكد_يساوي(مكمل_عكسي("AAAA"), "TTTT", "أدنين فقط")
# apl-source:58
تأكد_يساوي(مكمل_عكسي("ATCG"), "CGAT", "مختلط")
# apl-source:59
تأكد_يساوي(مكمل_عكسي(مكمل_عكسي("ATGCCGTA")), "ATGCCGTA", "عكسان يرجعان الأصل")
# apl-source:60
تأكد_يساوي(مكمل_عكسي("AAATTT"), "AAATTT", "متناظرة ذاتيا")
# apl-source:61
print("ATGCCGTA بالعكس:", مكمل_عكسي("ATGCCGTA"))
# apl-source:62
