info = {} # empty dict
days = set() # empty set

days = {"saturday","sunday","sunday","saturday"}
print(days)
print()

nums = [1,1,1,1,2,2,2,3,3,4,6.4,6.4,0,-1,-4]
nums = list(set(nums))# convert to set to remove duplicates, then back to list
print(nums)# order is not preserved, and duplicates are removed
print()

print(type(info))# dict
print(type(days))# set   
print()

servers = [
    "server1",
    "server1",
    "server2",
    "server2",
    "server3"
]

unique_servers = set(servers)
print(unique_servers)
print(f"Unique servers: {len(unique_servers)}")
print(f"Total servers: {len(servers)}")

