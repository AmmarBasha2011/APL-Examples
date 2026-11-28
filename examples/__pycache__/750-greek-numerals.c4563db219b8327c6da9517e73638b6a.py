
# apl-source:1
# مثال 750 — أرقام إغريقية
# apl-source:2
# Greek numerals
# apl-source:3
# Demonstrates: جداول حروف، ϝ ϟ ϡ، منازل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/750-greek-numerals.apl
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
# الأرقام الإغريقية (النظام الأيوني): حروف للآحاد والعشرات والمئات
# apl-source:25
# Demonstrates: ثلاثة جداول حروف, حروف أرشيفية ϝ ϟ ϡ, تركيب منازل
# apl-source:26
# ϝ=6 وϟ=90 وϡ=900 حروف سقطت من الأبجدية وبقيت في الأرقام
# apl-source:27

# apl-source:28
آحاد = ["", "α", "β", "γ", "δ", "ε", "ϝ", "ζ", "η", "θ"]
# apl-source:29
عشرات = ["", "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π", "ϟ"]
# apl-source:30
مئات = ["", "ρ", "σ", "τ", "υ", "φ", "χ", "ψ", "ω", "ϡ"]
# apl-source:31

# apl-source:32
def إلى_إغريقي(عدد):
  # apl-source:33
  if عدد <= 0 or عدد > 999:
    # apl-source:34
    return ""
  # apl-source:35
  return مئات[عدد // 100] + عشرات[(عدد // 10) % 10] + آحاد[عدد % 10]
# apl-source:36

# apl-source:37
def قيمة_إغريقية(حروف):
  # apl-source:38
  قيم = {}
  # apl-source:39
  for ي in range(1, 10):
    # apl-source:40
    قيم[آحاد[ي]] = ي
    # apl-source:41
    قيم[عشرات[ي]] = ي * 10
    # apl-source:42
    قيم[مئات[ي]] = ي * 100
  # apl-source:43
  مجموع = 0
  # apl-source:44
  for ي in range(len(حروف)):
    # apl-source:45
    مجموع = مجموع + قيم.get(حروف[ي], 0)
  # apl-source:46
  return مجموع
# apl-source:47

# apl-source:48
تأكد_يساوي(إلى_إغريقي(5), "ε", "خمسة")
# apl-source:49
تأكد_يساوي(إلى_إغريقي(7), "ζ", "سبعة")
# apl-source:50
تأكد_يساوي(إلى_إغريقي(42), "μβ", "اثنان وأربعون")
# apl-source:51
تأكد_يساوي(إلى_إغريقي(100), "ρ", "مئة")
# apl-source:52
تأكد_يساوي(إلى_إغريقي(365), "τξε", "أيام السنة")
# apl-source:53
تأكد_يساوي(إلى_إغريقي(999), "ϡϟθ", "تسعمئة وتسعة وتسعون")
# apl-source:54
تأكد_يساوي(إلى_إغريقي(0), "", "صفر غير موجود")
# apl-source:55

# apl-source:56
تأكد_يساوي(قيمة_إغريقية("μβ"), 42, "قراءة عكسية")
# apl-source:57
تأكد_يساوي(قيمة_إغريقية("ϡϟθ"), 999, "الحروف الأرشيفية")
# apl-source:58
تأكد_يساوي(قيمة_إغريقية(إلى_إغريقي(613)), 613, "ذهاب وإياب")
# apl-source:59

# apl-source:60
print("888 =", إلى_إغريقي(888))
# apl-source:61
