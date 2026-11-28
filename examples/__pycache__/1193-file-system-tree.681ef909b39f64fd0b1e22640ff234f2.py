
# apl-source:1
# مثال 1193 — نظام ملفات
# apl-source:2
# In-memory file system
# apl-source:3
# Demonstrates: قواميس متداخلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1193-file-system-tree.apl
# apl-source:6

# apl-source:7
# كل مجلد قاموس يحوي مجلدات فرعية
# apl-source:8
# والملف نص مخزن تحت اسمه
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
class نظام_ملفات:
  # apl-source:19
  def __init__(ذات):
    # apl-source:20
    ذات.جذر = {}
# apl-source:21

  # apl-source:22
  def اجزاء(ذات, مسار):
    # apl-source:23
    ناتج = []
    # apl-source:24
    for ج in مسار.split("/"):
      # apl-source:25
      if ج != "":
        # apl-source:26
        ناتج = ناتج + [ج]
    # apl-source:27
    return ناتج
# apl-source:28

  # apl-source:29
  def انشئ_مجلد(ذات, مسار):
    # apl-source:30
    عقدة = ذات.جذر
    # apl-source:31
    for ج in ذات.اجزاء(مسار):
      # apl-source:32
      if ج not in عقدة:
        # apl-source:33
        عقدة[ج] = {}
      # apl-source:34
      عقدة = عقدة[ج]
# apl-source:35

  # apl-source:36
  def اكتب(ذات, مسار, نص_):
    # apl-source:37
    ج = ذات.اجزاء(مسار)
    # apl-source:38
    عقدة = ذات.جذر
    # apl-source:39
    for ع in range(len(ج) - 1):
      # apl-source:40
      if ج[ع] not in عقدة:
        # apl-source:41
        عقدة[ج[ع]] = {}
      # apl-source:42
      عقدة = عقدة[ج[ع]]
    # apl-source:43
    عقدة[ج[-1]] = نص_
# apl-source:44

  # apl-source:45
  def اقرأ(ذات, مسار):
    # apl-source:46
    عقدة = ذات.جذر
    # apl-source:47
    for ج in ذات.اجزاء(مسار):
      # apl-source:48
      عقدة = عقدة[ج]
    # apl-source:49
    return عقدة
# apl-source:50

  # apl-source:51
  def اعرض(ذات, مسار):
    # apl-source:52
    عقدة = ذات.جذر
    # apl-source:53
    for ج in ذات.اجزاء(مسار):
      # apl-source:54
      عقدة = عقدة[ج]
    # apl-source:55
    if type(عقدة) == type({}):
      # apl-source:56
      return sorted(list(عقدة))
    # apl-source:57
    return [ذات.اجزاء(مسار)[-1]]
# apl-source:58

# apl-source:59
ن = نظام_ملفات()
# apl-source:60
ن.انشئ_مجلد("/a/b")
# apl-source:61
ن.اكتب("/a/b/c.txt", "hello")
# apl-source:62
ن.اكتب("/a/d.txt", "world")
# apl-source:63
تأكد_يساوي(ن.اعرض("/"), ["a"], "الجذر")
# apl-source:64
تأكد_يساوي(ن.اعرض("/a"), ["b", "d.txt"], "مجلد a")
# apl-source:65
تأكد_يساوي(ن.اقرأ("/a/b/c.txt"), "hello", "قراءة ملف")
# apl-source:66
تأكد_يساوي(ن.اعرض("/a/d.txt"), ["d.txt"], "عرض ملف")
# apl-source:67
