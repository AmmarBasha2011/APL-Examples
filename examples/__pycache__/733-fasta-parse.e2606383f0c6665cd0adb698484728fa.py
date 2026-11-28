
# apl-source:1
# مثال 733 — تحليل FASTA
# apl-source:2
# FASTA parsing
# apl-source:3
# Demonstrates: عناوين، سجلات، دمج سطور
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/733-fasta-parse.apl
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
# تحليل ملف FASTA (تنسيق تسلسلات جينية)
# apl-source:25
# Demonstrates: سطور تبدأ بـ >, بناء قاموس سجلات, تجميع تسلسل متعدد السطور
# apl-source:26
# كل سجل يبدأ بسطر عنوان >id ثم سطور تسلسل تُدمج
# apl-source:27

# apl-source:28
def حلل_fasta(سطور):
  # apl-source:29
  سجلات = {}
  # apl-source:30
  ترتيب = []
  # apl-source:31
  حالي = None
  # apl-source:32
  for سطر in سطور:
    # apl-source:33
    if سطر.startswith(">"):
      # apl-source:34
      حالي = سطر[1:len(سطر)]
      # apl-source:35
      سجلات[حالي] = ""
      # apl-source:36
      ترتيب.append(حالي)
    # apl-source:37
    elif حالي != None:
      # apl-source:38
      سجلات[حالي] = سجلات[حالي] + سطر
  # apl-source:39
  return [ترتيب, سجلات]
# apl-source:40

# apl-source:41
def أطوال(سطور):
  # apl-source:42
  ناتج = حلل_fasta(سطور)
  # apl-source:43
  ترتيب = ناتج[0]
  # apl-source:44
  سجلات = ناتج[1]
  # apl-source:45
  قياسات = {}
  # apl-source:46
  for مفتاح in ترتيب:
    # apl-source:47
    قياسات[مفتاح] = len(سجلات[مفتاح])
  # apl-source:48
  return قياسات
# apl-source:49

# apl-source:50
def أطول_سجل(سطور):
  # apl-source:51
  ناتج = حلل_fasta(سطور)
  # apl-source:52
  ترتيب = ناتج[0]
  # apl-source:53
  سجلات = ناتج[1]
  # apl-source:54
  أفضل = ترتيب[0]
  # apl-source:55
  for مفتاح in ترتيب:
    # apl-source:56
    if len(سجلات[مفتاح]) > len(سجلات[أفضل]):
      # apl-source:57
      أفضل = مفتاح
  # apl-source:58
  return [أفضل, len(سجلات[أفضل])]
# apl-source:59

# apl-source:60
عينة = [">seq1", "ATGC", "ATGC", ">seq2", "GG", "CC", ">seq3", "A"]
# apl-source:61
ناتج = حلل_fasta(عينة)
# apl-source:62
ترتيب = ناتج[0]
# apl-source:63
سجلات = ناتج[1]
# apl-source:64

# apl-source:65
تأكد_يساوي(ترتيب, ["seq1", "seq2", "seq3"], "ترتيب السجلات")
# apl-source:66
تأكد_يساوي(سجلات["seq1"], "ATGCATGC", "دمج سطرين")
# apl-source:67
تأكد_يساوي(سجلات["seq2"], "GGCC", "سجل ثان")
# apl-source:68
تأكد_يساوي(سجلات["seq3"], "A", "سجل قصير")
# apl-source:69

# apl-source:70
قياسات = أطوال(عينة)
# apl-source:71
تأكد_يساوي(قياسات["seq1"], 8, "طول الأول")
# apl-source:72
تأكد_يساوي(قياسات["seq3"], 1, "طول الثالث")
# apl-source:73
تأكد_يساوي(أطول_سجل(عينة), ["seq1", 8], "الأطول")
# apl-source:74

# apl-source:75
تأكد_يساوي(len(حلل_fasta([">x", "AC"])[0]), 1, "سجل واحد")
# apl-source:76
تأكد_يساوي(حلل_fasta(["AC", "GT"])[0], [], "بلا عناوين")
# apl-source:77

# apl-source:78
print("سجلات:", len(ترتيب))
# apl-source:79
print("seq1:", سجلات["seq1"])
# apl-source:80
