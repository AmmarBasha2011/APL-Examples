
# apl-source:1
# مثال 1344 — حساب القسمة
# apl-source:2
# Evaluate division queries
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1344-evaluate-division.apl
# apl-source:6

# apl-source:7
# كل معادلة حافة موزونة في رسم بياني
# apl-source:8
# نبحث عن مسار ونضرب الأوزان
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
def احسب_القسمة(معادلات, قيم, استعلامات):
  # apl-source:19
  جيران = {}
  # apl-source:20
  for ع in range(len(معادلات)):
    # apl-source:21
    أ = معادلات[ع][0]
    # apl-source:22
    ب = معادلات[ع][1]
    # apl-source:23
    if أ not in جيران:
      # apl-source:24
      جيران[أ] = []
    # apl-source:25
    if ب not in جيران:
      # apl-source:26
      جيران[ب] = []
    # apl-source:27
    جيران[أ] = جيران[أ] + [[ب, قيم[ع]]]
    # apl-source:28
    جيران[ب] = جيران[ب] + [[أ, 1.0 / قيم[ع]]]
  # apl-source:29
  نتائج = []
  # apl-source:30
  for س in استعلامات:
    # apl-source:31
    if (س[0] not in جيران) or (س[1] not in جيران):
      # apl-source:32
      نتائج = نتائج + [-1.0]
    # apl-source:33
    else:
      # apl-source:34
      مرئي = {}
      # apl-source:35
      مرئي[س[0]] = True
      # apl-source:36
      مكدس = [[س[0], 1.0]]
      # apl-source:37
      جواب = -1.0
      # apl-source:38
      while len(مكدس) > 0:
        # apl-source:39
        ن = مكدس.pop()
        # apl-source:40
        if ن[0] == س[1]:
          # apl-source:41
          جواب = ن[1]
        # apl-source:42
        for ج in جيران[ن[0]]:
          # apl-source:43
          if ج[0] not in مرئي:
            # apl-source:44
            مرئي[ج[0]] = True
            # apl-source:45
            مكدس = مكدس + [[ج[0], ن[1] * ج[1]]]
      # apl-source:46
      نتائج = نتائج + [جواب]
  # apl-source:47
  return نتائج
# apl-source:48

# apl-source:49
م = [["a","b"],["b","c"]]
# apl-source:50
ق = [2.0, 3.0]
# apl-source:51
تأكد_يساوي(احسب_القسمة(م, ق, [["a","c"]]), [6.0], "نسبة غير مباشرة")
# apl-source:52
تأكد_يساوي(احسب_القسمة(م, ق, [["b","a"]]), [0.5], "نسبة معكوسة")
# apl-source:53
تأكد_يساوي(احسب_القسمة(م, ق, [["a","x"]]), [-1.0], "متغير مجهول")
# apl-source:54
