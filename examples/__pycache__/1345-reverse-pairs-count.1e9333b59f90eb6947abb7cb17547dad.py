
# apl-source:1
# مثال 1345 — الأزواج المعكوسة
# apl-source:2
# Reverse pairs count
# apl-source:3
# Demonstrates: فرز ودمج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1345-reverse-pairs-count.apl
# apl-source:6

# apl-source:7
# نستخدم فرز الدمج
# apl-source:8
# وقبل كل دمج نعد الأزواج بمؤشرين
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
def عد_معكوسة(أرقام):
  # apl-source:19
  if len(أرقام) <= 1:
    # apl-source:20
    return [0, أرقام[:]]
  # apl-source:21
  وسط = len(أرقام) // 2
  # apl-source:22
  يس = عد_معكوسة(أرقام[:وسط])
  # apl-source:23
  يم = عد_معكوسة(أرقام[وسط:])
  # apl-source:24
  عدد = يس[0] + يم[0]
  # apl-source:25
  أ = يس[1]
  # apl-source:26
  ب = يم[1]
  # apl-source:27
  ج = 0
  # apl-source:28
  for ع in range(len(أ)):
    # apl-source:29
    while (ج < len(ب)) and (أ[ع] > 2 * ب[ج]):
      # apl-source:30
      ج = ج + 1
    # apl-source:31
    عدد = عدد + ج
  # apl-source:32
  return [عدد, sorted(أ + ب)]
# apl-source:33

# apl-source:34
تأكد_يساوي(عد_معكوسة([1,3,2,3,1])[0], 2, "اثنان")
# apl-source:35
تأكد_يساوي(عد_معكوسة([2,4,3,5,1])[0], 3, "ثلاثة")
# apl-source:36
تأكد_يساوي(عد_معكوسة([1,2,3])[0], 0, "لا أزواج")
# apl-source:37
