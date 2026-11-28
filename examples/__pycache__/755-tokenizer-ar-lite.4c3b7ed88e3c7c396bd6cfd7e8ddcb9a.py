
# apl-source:1
# مثال 755 — مجزئ عربي
# apl-source:2
# Arabic tokenizer
# apl-source:3
# Demonstrates: آلة حالات، مدى يونيكود، ترقيم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/755-tokenizer-ar-lite.apl
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
# مجزئ نصوص عربية: كلمات وأرقام وعلامات ترقيم
# apl-source:25
# Demonstrates: آلة حالات, مدى الحروف العربية في يونيكود, أرقام عشرية
# apl-source:26
# الحروف العربية U+0621..U+064A، وعلامات الترقيم تنفصل كوحدات
# apl-source:27

# apl-source:28
def صنف_حرف(حرف):
  # apl-source:29
  نقطة = ord(حرف)
  # apl-source:30
  if نقطة >= 1569 and نقطة <= 1618:
    # apl-source:31
    return "كلمة"
  # apl-source:32
  if حرف >= "0" and حرف <= "9":
    # apl-source:33
    return "رقم"
  # apl-source:34
  if نقطة >= 1632 and نقطة <= 1641:
    # apl-source:35
    return "رقم"
  # apl-source:36
  return "أخرى"
# apl-source:37

# apl-source:38
def مجزئ(نص):
  # apl-source:39
  وحدات = []
  # apl-source:40
  حالي = ""
  # apl-source:41
  صنف = ""
  # apl-source:42
  for ي in range(len(نص)):
    # apl-source:43
    حرف = نص[ي]
    # apl-source:44
    ج = صنف_حرف(حرف)
    # apl-source:45
    if ج == "أخرى":
      # apl-source:46
      if حالي != "":
        # apl-source:47
        وحدات.append([صنف, حالي])
        # apl-source:48
        حالي = ""
        # apl-source:49
        صنف = ""
      # apl-source:50
      if حرف != " ":
        # apl-source:51
        وحدات.append(["ترقيم", حرف])
    # apl-source:52
    elif ج == صنف:
      # apl-source:53
      حالي = حالي + حرف
    # apl-source:54
    else:
      # apl-source:55
      if حالي != "":
        # apl-source:56
        وحدات.append([صنف, حالي])
      # apl-source:57
      حالي = حرف
      # apl-source:58
      صنف = ج
  # apl-source:59
  if حالي != "":
    # apl-source:60
    وحدات.append([صنف, حالي])
  # apl-source:61
  return وحدات
# apl-source:62

# apl-source:63
def كلمات_فقط(نص):
  # apl-source:64
  ناتج = []
  # apl-source:65
  for وحدة in مجزئ(نص):
    # apl-source:66
    if وحدة[0] == "كلمة":
      # apl-source:67
      ناتج.append(وحدة[1])
  # apl-source:68
  return ناتج
# apl-source:69

# apl-source:70
وحدات = مجزئ("مرحباً بالعالم! رقم 42.")
# apl-source:71
تأكد_يساوي(وحدات[0], ["كلمة", "مرحباً"], "أول كلمة")
# apl-source:72
تأكد_يساوي(وحدات[1], ["كلمة", "بالعالم"], "ثاني كلمة")
# apl-source:73
تأكد_يساوي(وحدات[2], ["ترقيم", "!"], "علامة تعجب")
# apl-source:74
تأكد_يساوي(وحدات[4], ["رقم", "42"], "رقم")
# apl-source:75
تأكد_يساوي(وحدات[5], ["ترقيم", "."], "نقطة")
# apl-source:76

# apl-source:77
تأكد_يساوي(كلمات_فقط("العلم نور والجهل ظلام"), ["العلم", "نور", "والجهل", "ظلام"], "جملة بلا ترقيم")
# apl-source:78
تأكد_يساوي(len(مجزئ("")), 0, "نص فارغ")
# apl-source:79
تأكد_يساوي(مجزئ("٣٤٥"), [["رقم", "٣٤٥"]], "أرقام عربية مشرقية")
# apl-source:80

# apl-source:81
print("الكلمات:", كلمات_فقط("مرحباً بالعالم! رقم 42."))
# apl-source:82
