# Infosoft_assignment


Problem #3 - Debug Calendar Design  :

Step 1: First run the program and analyze the output.

Step 2: After analyzing the program and output, the insertion of value is only for left_child and not for right_child.So, added right_child.

Step 3: After analyzing the first if condition "if node.start <= self.end" is not as per the requirement. So, I changed that condition.

Step 3: Once condition changed, I added return False as per the requirement.


Underlying Issues: 
    The issue is with
    1. if condition.
    2. Insertion of node into child.
    3. At the time of Double booking False is not returned.
