
# apl-source:1
# مثال 937 — ضغط LZW
# apl-source:2
# LZW compression
# apl-source:3
# Demonstrates: قاموس ينمو أثناء القراءة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/937-lzw.apl
# apl-source:6

# apl-source:7
# ضغط LZW: قاموس يكبر أثناء القراءة بلا نوافذ
# apl-source:8
# أساس GIF و compress
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
# قاموس: قوائم متوازية (سلسلة، رمز)
# apl-source:19
def ابحث_قاموس(سلاسل, هدف):
  # apl-source:20
  for i in range(len(سلاسل)):
    # apl-source:21
    if سلاسل[i] == هدف:
      # apl-source:22
      return i
  # apl-source:23
  return -1
# apl-source:24

# apl-source:25
def اضغط(نص):
  # apl-source:26
  سلاسل = []
  # apl-source:27
  رموز = []
  # apl-source:28
  # القاموس الأولي: كل حرف منفرد موجود في النص
  # apl-source:29
  for i in range(len(نص)):
    # apl-source:30
    حرف = نص[i]
    # apl-source:31
    if ابحث_قاموس(سلاسل, حرف) < 0:
      # apl-source:32
      سلاسل = سلاسل + [حرف]
      # apl-source:33
      رموز = رموز + [ord(حرف)]
  # apl-source:34
  تالي = 256
  # apl-source:35
  خرج = []
  # apl-source:36
  جاري = ""
  # apl-source:37
  for i in range(len(نص)):
    # apl-source:38
    حرف = نص[i]
    # apl-source:39
    مرشح = جاري + حرف
    # apl-source:40
    if ابحث_قاموس(سلاسل, مرشح) >= 0:
      # apl-source:41
      جاري = مرشح
    # apl-source:42
    else:
      # apl-source:43
      خرج = خرج + [رموز[ابحث_قاموس(سلاسل, جاري)]]
      # apl-source:44
      سلاسل = سلاسل + [مرشح]
      # apl-source:45
      رموز = رموز + [تالي]
      # apl-source:46
      تالي = تالي + 1
      # apl-source:47
      جاري = حرف
  # apl-source:48
  if جاري != "":
    # apl-source:49
    خرج = خرج + [رموز[ابحث_قاموس(سلاسل, جاري)]]
  # apl-source:50
  return خرج
# apl-source:51

# apl-source:52
ناتج = اضغط("TOBEORNOTTOBEORTOBEORNOT")
# apl-source:53
print("الرموز:", ناتج)
# apl-source:54

# apl-source:55
متوقع = [84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258, 260, 265, 259, 261, 263]
# apl-source:56
تأكد_يساوي(len(ناتج), 16, "16 رمزاً")
# apl-source:57
for i in range(16):
  # apl-source:58
  تأكد_يساوي(ناتج[i], متوقع[i], "رمز " + str(i))
# apl-source:59

# apl-source:60
# نص من 25 حرفاً يضغط إلى 16 رمزاً
# apl-source:61
if len(ناتج) >= len("TOBEORNOTTOBEORTOBEORNOT"):
  # apl-source:62
  print("فشل: لم يحدث ضغط")
  # apl-source:63
  قياسي_نظام_اخرج(1)
# apl-source:64
print("ناجح: ضغط فعلي")
# apl-source:65
