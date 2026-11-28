
# apl-source:1
# مثال 901 — أقل تدوير أبجدي
# apl-source:2
# Minimal rotation
# apl-source:3
# Demonstrates: خوارزمية بوث الخطية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/901-minimal-rotation.apl
# apl-source:6

# apl-source:7
# أقل تدوير أبجدياً لسلسلة: خوارزمية بوث O(n)
# apl-source:8
# تستخدم في مطابقة السلاسل الدائرية
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
def أقل_تدوير(سلسلة):
  # apl-source:19
  س = سلسلة + سلسلة
  # apl-source:20
  ن = len(سلسلة)
  # apl-source:21
  i = 0
  # apl-source:22
  ج = 1
  # apl-source:23
  ق = 0
  # apl-source:24
  while (i < ن) and (ج < ن) and (ق < ن):
    # apl-source:25
    if س[i + ق] == س[ج + ق]:
      # apl-source:26
      ق = ق + 1
    # apl-source:27
    elif س[i + ق] > س[ج + ق]:
      # apl-source:28
      i = i + ق + 1
      # apl-source:29
      if i <= ج:
        # apl-source:30
        i = ج + 1
      # apl-source:31
      ق = 0
    # apl-source:32
    else:
      # apl-source:33
      ج = ج + ق + 1
      # apl-source:34
      if ج <= i:
        # apl-source:35
        ج = i + 1
      # apl-source:36
      ق = 0
  # apl-source:37
  if i < ج:
    # apl-source:38
    return i
  # apl-source:39
  return ج
# apl-source:40

# apl-source:41
print("bbabaa ->", أقل_تدوير("bbabaa"))
# apl-source:42
print("bcabcab ->", أقل_تدوير("bcabcab"))
# apl-source:43

# apl-source:44
تأكد_يساوي(أقل_تدوير("bbabaa"), 4, "bbabaa تدويرها الأدنى aabbab من 4")
# apl-source:45
تأكد_يساوي(أقل_تدوير("bcabcab"), 5, "bcabcab تدويرها الأدنى abbcabc من 5")
# apl-source:46
تأكد_يساوي(أقل_تدوير("aaa"), 0, "متماثلة")
# apl-source:47
تأكد_يساوي(أقل_تدوير("ba"), 1, "ba -> ab من 1")
# apl-source:48
