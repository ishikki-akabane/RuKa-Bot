
"""
MeowCore Centralized Federation System

This module defines the structure and functionality for managing a centralized federation system where various federations can share and access lists of users who have been flagged for inappropriate or harmful behavior.
Each federation is managed by an owner and designated administrators who can update the list based on specific reasons and categories.

All rights reserved by MeowCore Team ©.

Database Structure:

1. Federation Information:
   - uuid (str): A unique identifier for each federation (Primary Key).
   - owner_id (str): The unique identifier of the federation's owner or creator.
   - owner_name (str): The name of the owner or creator of the federation.
   - fed_type (str): Indicates the visibility status of the federation, either 'public' or 'private'.
   - access_list (list[str]): A list of authorized users or federations permitted to access this federation's data. If empty, the federation is public.

2. Admin Management:
   - admin_list (list[dict]): A list of administrators responsible for managing the federation and updating the list of flagged users.
       - admin_id (str): The unique identifier for each admin.
       - admin_name (str): The name of each admin.

3. Flagged Users List:
   - flagged_users (list[dict]): A collection of users flagged for inappropriate or harmful behavior.
       - user_id (str): The unique identifier of the flagged user.
       - user_name (str): The name of the flagged user.
       - reason (str): The reason or explanation for flagging the user.
       - date (str): The date when the person was flagged
       - tags (list[str]): Categories that describe the nature of the user’s behavior (e.g., spamming, hate speech).
       - flagged_by (dict): Information about the admin who flagged the user.
           - admin_id (str): The unique identifier of the admin who flagged the user.
           - admin_name (str): The name of the admin who flagged the user.
           - fed_uuid (str): The unique identifier of the federation where the user was flagged.

Tags for Flagged Users:
The system uses specific categories, known as tags, to classify different types of inappropriate or harmful behavior. The following are suggested tags:

   1. Spamming
   2. NSFW Content
   3. Hate Speech
   4. Terrorism
   5. Promotion of Illegal Activities
   6. Harassment
   7. Phishing
   8. Impersonation
   9. Misinformation/Disinformation
   10. Fraud
   11. Cyberbullying
   12. Racism
   13. Homophobia
   14. Extortion
   15. Child Exploitation
   16. Malware Distribution
   17. Doxxing
   18. Unauthorized Access Attempts
   19. Botting
   20. Scamming

This structure provides a scalable and flexible solution for federations to manage and share their flagged users' lists, improving collective safety by enabling access to trusted user data across multiple federations.

Usage:
The system allows federations to maintain their own flagged users' lists and share them with others. It offers flexibility in determining who can access the list, allowing federations to set public or private access levels.
"""

