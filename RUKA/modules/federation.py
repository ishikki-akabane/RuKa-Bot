"""
All rights to this centralised federation module reserved with MeowCore Team

database structure:
uuid - federation unique id
owner_id and owner_name - info of the creator/owner
admin_list - list of Admins who can modify the federation
  - admin id and admin name - info of the admin
scanned - list of scanned people found as malicious
  - user_id
  - user name
  - reason
  - tag - tags for malicious people
    - []
  - scanned
    - admin id
    - admin name
    - fed_uuid
fed_type - public or private
access - list of people who can use it, empty in case of public fed
"""
