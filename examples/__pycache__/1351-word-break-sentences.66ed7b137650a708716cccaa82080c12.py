
# apl-source:1
# مثال 1351 — جمل من كلمات
# apl-source:2
# Word break all sentences
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1351-word-break-sentences.apl
# apl-source:6

# apl-source:7
# نجرب كل بادئة موجودة في القاموس
# apl-source:8
# ونكمل بالتراجع على الباقي
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
def كل_الجمل(نص_, قاموس):
  # apl-source:19
  ذاكرة = {}
  # apl-source:20
  def حل(بداية):
    # apl-source:21
    if بداية in ذاكرة:
      # apl-source:22
      return ذاكرة[بداية]
    # apl-source:23
    if بداية == len(نص_):
      # apl-source:24
      return [""]
    # apl-source:25
    نتائج = []
    # apl-source:26
    for نهاية in range(بداية + 1, len(نص_) + 1):
      # apl-source:27
      كلمة = نص_[بداية:نهاية]
      # apl-source:28
      if كلمة in قاموس:
        # apl-source:29
        for بقية in حل(نهاية):
          # apl-source:30
          if بقية == "":
            # apl-source:31
            نتائج = نتائج + [كلمة]
          # apl-source:32
          else:
            # apl-source:33
            نتائج = نتائج + [كلمة + " " + بقية]
    # apl-source:34
    ذاكرة[بداية] = نتائج
    # apl-source:35
    return نتائج
  # apl-source:36
  return sorted(حل(0))
# apl-source:37

# apl-source:38
تأكد_يساوي(كل_الجمل("catsanddog", ["cat","cats","and","sand","dog"]), ["cat sand dog","cats and dog"], "جملتان")
# apl-source:39
تأكد_يساوي(كل_الجمل("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]), ["pine apple pen apple","pine applepen apple","pineapple pen apple"], "ثلاث جمل")
# apl-source:40
تأكد_يساوي(كل_الجمل("catsandog", ["cats","dog","sand","and","cat"]), [], "لا جملة")
# apl-source:41
