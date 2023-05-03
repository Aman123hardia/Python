list(range(3, 6))            # normal call with separate arguments

print(list)
args = [3, 6]

print(list(range(args),"ama"))            # call with arguments unpacked from a list


