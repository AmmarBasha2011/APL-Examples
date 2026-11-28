
# apl-source:1
# مثال 1777 — تبسيط مسار يونكس
# apl-source:2
# Simplify a Unix path
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1777-simplify-unix-path.apl
# apl-source:6

# apl-source:7
# نقسم بالشرطة المائلة
# apl-source:8
# النقطتان تعيدان مستوى
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
def بسّط(مسار):
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
    elif ج != "" and ج != ".":
      # apl-source:25
      مكدس.append(ج)
  # apl-source:26
  return "/" + "/".join(مكدس)
# apl-source:27

# apl-source:28
تأكد_يساوي(بسّط("/a/./b/../c/"), "/a/c", "مختلط")
# apl-source:29
تأكد_يساوي(بسّط("/../"), "/", "الجذر")
# apl-source:30
تأكد_يساوي(بسّط("/home//foo/"), "/home/foo", "مزدوجة")
# apl-source:31
