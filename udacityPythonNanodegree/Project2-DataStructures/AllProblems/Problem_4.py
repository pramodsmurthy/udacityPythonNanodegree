class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):    
    user_in_group = False

    if len(group.get_groups) == 0 and len(group.get_users) == 0:
        return user_in_group

    for u in group.get_users():
        if u == user:
            return True
    
    for g in group.get_groups():
        user_in_group = is_user_in_group(user, g)
        if user_in_group:
            break
    
    if user_in_group:
        return "User is in group"
    else:
        return "User not in group"

def add(group, count, isGroup):
    if isGroup == "group":
        for i in range(count):
            gname = group.get_name()
            gobj = Group(gname+"_group"+str(i))
            group.add_group(gobj)
    else:
        for i in range(count):
            group.add_user(group.get_name()+"_user"+str(i))
        
# Test Case 1
# No groups, no users
parent = Group("parent")
expected_output1 = "User not in group"
output1 = (is_user_in_group("parent_user", parent))
#print(f"Expected Output: {expected_output1}")

# Test Case 2
# Multiple Groups and users, given user is present
add(parent, 5, "group")  # Add 5 groups to parent
add(parent, 50, "user")  # Add 50 users to parent group
child = Group("child")
add(child, 3, "group")  # Add 3 groups to child group
add(child, 10, "user")  # Add 10 users to child group
child_groupxx = Group("child_groupxx")
parent.add_group(child_groupxx) # Add child_group1 to parent
child_groupxx.add_user("Alexa") # Add alexa user to child_group1
expected_output2 = "User is in group"
output2 = is_user_in_group("Alexa", parent)  # Search for alexa user in parent group
#print(f"Expected Output: {expected_output2}")

# Test Case 3
# Multiple groups and users, given user is not present
expected_output3 = "User not in group"
output3 = is_user_in_group("Alex", parent)
#print(f"Expected Output: {expected_output3}")


#print("True" if output1 == expected_output1 else "False")
#print("True" if output2 == expected_output2 else "False")
#print("True" if output3 == expected_output3 else "False")
