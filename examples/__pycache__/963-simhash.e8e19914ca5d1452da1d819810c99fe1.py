
# apl-source:1
# مثال 963 — بصمة سيمهاش
# apl-source:2
# SimHash fingerprint
# apl-source:3
# Demonstrates: تصويت بالإشارة على البتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/963-simhash.apl
# apl-source:6

# apl-source:7
# التجزئة التشابهية (سيمهاش): بصمة 16 بت تقارب الوثائق المتشابهة
# apl-source:8
# كل رمز يصوت بموجب أو سالب على كل بت ثم تؤخذ إشارة المحصلة
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
def هاش16(رمز):
  # apl-source:19
  ح = 0
  # apl-source:20
  for i in range(len(رمز)):
    # apl-source:21
    ح = ((ح * 31) + ord(رمز[i])) % 65536
  # apl-source:22
  return ح
# apl-source:23

# apl-source:24
def بصمة(وثيقة):
  # apl-source:25
  رموز = وثيقة.split(" ")
  # apl-source:26
  تصويت = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  # apl-source:27
  for رمز in رموز:
    # apl-source:28
    ح = هاش16(رمز)
    # apl-source:29
    for بت in range(16):
      # apl-source:30
      if (ح & (1 << بت)) != 0:
        # apl-source:31
        تصويت[بت] = تصويت[بت] + 1
      # apl-source:32
      else:
        # apl-source:33
        تصويت[بت] = تصويت[بت] - 1
  # apl-source:34
  ب = 0
  # apl-source:35
  for بت in range(16):
    # apl-source:36
    if تصويت[بت] > 0:
      # apl-source:37
      ب = ب | (1 << بت)
  # apl-source:38
  return ب
# apl-source:39

# apl-source:40
def هامنغ(أ, ب):
  # apl-source:41
  س = أ ^ ب
  # apl-source:42
  عد = 0
  # apl-source:43
  while س > 0:
    # apl-source:44
    عد = عد + (س & 1)
    # apl-source:45
    س = س >> 1
  # apl-source:46
  return عد
# apl-source:47

# apl-source:48
تأكد_يساوي(هاش16("the"), 49265, "هاش الرمز")
# apl-source:49
ب1 = بصمة("the cat sat on the mat")
# apl-source:50
ب2 = بصمة("the rat sat on the mat")
# apl-source:51
تأكد_يساوي(ب1, 33136, "بصمة الوثيقة الأولى")
# apl-source:52
تأكد_يساوي(ب2, 32865, "بصمة الوثيقة الثانية")
# apl-source:53
تأكد_يساوي(هامنغ(ب1, ب2), 3, "تقارب البصمتين")
# apl-source:54
