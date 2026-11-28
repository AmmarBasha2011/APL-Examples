
# apl-source:1
# مثال 1240 — تبسيط مسار
# apl-source:2
# Simplify unix path
# apl-source:3
# Demonstrates: مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1240-simplify-path.apl
# apl-source:6

# apl-source:7
# النقطتان ترجعان مجلداً
# apl-source:8
# والنقطة وعلامة الشرطة المكررة تتجاهلان
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
def بسط(مسار):
  # apl-source:19
  مكدس = []
  # apl-source:20
  for ج in مسار.split("/"):
    # apl-source:21
    if ج == "..":
      # apl-source:22
      if len(مكدس) > 0:
        # apl-source:23
        مكدس.pop()
    # apl-source:24
    elif (ج != "") and (ج != "."):
      # apl-source:25
      مكدس = مكدس + [ج]
  # apl-source:26
  return "/" + "/".join(مكدس)
# apl-source:27

# apl-source:28
تأكد_يساوي(بسط("/home/"), "/home", "شرطة أخيرة")
# apl-source:29
تأكد_يساوي(بسط("/../"), "/", "فوق الجذر")
# apl-source:30
تأكد_يساوي(بسط("/home//foo/"), "/home/foo", "شرطتان")
# apl-source:31
تأكد_يساوي(بسط("/a/./b/../../c/"), "/c", "مختلط")
# apl-source:32
