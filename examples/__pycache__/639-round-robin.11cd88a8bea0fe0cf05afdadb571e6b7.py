
# apl-source:1
# مثال 639 — جدولة بالتناوب الدائري
# apl-source:2
# Round robin scheduling
# apl-source:3
# Demonstrates: كم زمني، طابور جاهز، انتظار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/639-round-robin.apl
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
# جدولة المعالج بالتناوب الدائري (Round Robin)
# apl-source:25
# Demonstrates: كم زمني, طابور جاهز, أزمنة انتظار واستدارة
# apl-source:26
# كل عملية تأخذ حصتها ثم تعود لآخر الطابور
# apl-source:27

# apl-source:28
def جدول(عمليات, كم):
  # apl-source:29
  جاهز = []
  # apl-source:30
  for ي in range(len(عمليات)):
    # apl-source:31
    جاهز.append([ي, عمليات[ي]])
  # apl-source:32
  متبقي = عمليات.copy()
  # apl-source:33
  انتظار = [0] * len(عمليات)
  # apl-source:34
  انتهاء = [0] * len(عمليات)
  # apl-source:35
  زمن = 0
  # apl-source:36
  while len(جاهز) > 0:
    # apl-source:37
    حالي = جاهز.pop(0)
    # apl-source:38
    ي = حالي[0]
    # apl-source:39
    تنفيذ = min(كم, متبقي[ي])
    # apl-source:40
    for ج in range(len(عمليات)):
      # apl-source:41
      if ج != ي and متبقي[ج] > 0 and انتهاء[ج] == 0:
        # apl-source:42
        انتظار[ج] = انتظار[ج] + تنفيذ
    # apl-source:43
    زمن = زمن + تنفيذ
    # apl-source:44
    متبقي[ي] = متبقي[ي] - تنفيذ
    # apl-source:45
    if متبقي[ي] > 0:
      # apl-source:46
      جاهز.append([ي, متبقي[ي]])
    # apl-source:47
    else:
      # apl-source:48
      انتهاء[ي] = زمن
  # apl-source:49
  return [انتظار, انتهاء]
# apl-source:50

# apl-source:51
نتيجة = جدول([10, 4, 6], 3)
# apl-source:52
print("انتظار:", نتيجة[0], " انتهاء:", نتيجة[1])
# apl-source:53
تأكد_يساوي(نتيجة[1], [20, 13, 16], "أزمنة الانتهاء")
# apl-source:54
تأكد_يساوي(نتيجة[0], [10, 9, 10], "أزمنة الانتظار (الانتهاء ناقص التنفيذ)")
# apl-source:55
