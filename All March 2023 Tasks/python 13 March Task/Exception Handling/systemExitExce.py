
try:
    print("hloo")
    raise SystemExit()
except SystemExit:
    print("Specifying SystemExit in this block works.",SystemExit)