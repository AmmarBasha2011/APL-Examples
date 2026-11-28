
# apl-source:1
# مثال 1359 — أصغر نص بالتبديل
# apl-source:2
# Smallest string with swaps
# apl-source:3
# Demonstrates: اتحاد ووجد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1359-smallest-string-with-swaps.apl
# apl-source:6

# apl-source:7
# الأزواج المتصلة تكون مجموعة حرة الترتيب
# apl-source:8
# نرتب حروف كل مجموعة ونعيدها لمواضعها
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
def اصغر_نص(نص_, ازواج):
  # apl-source:19
  ن = len(نص_)
  # apl-source:20
  اب = []
  # apl-source:21
  for ع in range(ن):
    # apl-source:22
    اب = اب + [ع]
  # apl-source:23
  def جذر(س):
    # apl-source:24
    while اب[س] != س:
      # apl-source:25
      اب[س] = اب[اب[س]]
      # apl-source:26
      س = اب[س]
    # apl-source:27
    return س
  # apl-source:28
  for ز in ازواج:
    # apl-source:29
    أ = جذر(ز[0])
    # apl-source:30
    ب = جذر(ز[1])
    # apl-source:31
    if أ != ب:
      # apl-source:32
      اب[أ] = ب
  # apl-source:33
  مجموعات = {}
  # apl-source:34
  for ع in range(ن):
    # apl-source:35
    ج = جذر(ع)
    # apl-source:36
    if ج not in مجموعات:
      # apl-source:37
      مجموعات[ج] = []
    # apl-source:38
    مجموعات[ج] = مجموعات[ج] + [ع]
  # apl-source:39
  حروف = list(نص_)
  # apl-source:40
  for ج in مجموعات:
    # apl-source:41
    مواضع = مجموعات[ج]
    # apl-source:42
    اح = []
    # apl-source:43
    for م in مواضع:
      # apl-source:44
      اح = اح + [نص_[م]]
    # apl-source:45
    اح = sorted(اح)
    # apl-source:46
    for ك in range(len(مواضع)):
      # apl-source:47
      حروف[مواضع[ك]] = اح[ك]
  # apl-source:48
  ناتج = ""
  # apl-source:49
  for ح in حروف:
    # apl-source:50
    ناتج = ناتج + ح
  # apl-source:51
  return ناتج
# apl-source:52

# apl-source:53
تأكد_يساوي(اصغر_نص("dcab", [[0,3],[1,2]]), "bacd", "مجموعتان")
# apl-source:54
تأكد_يساوي(اصغر_نص("dcab", [[0,3],[1,2],[0,2]]), "abcd", "مجموعة واحدة")
# apl-source:55
تأكد_يساوي(اصغر_نص("cba", [[0,1],[1,2]]), "abc", "سلسلة")
# apl-source:56
