# DATABASE

## Data Structures
📘 **users**
- `_id` (BIGINT): Unique ID of the user (Telegram User ID, Primary Key)
- `name` (VARCHAR): Name of the user
- `bio` (TEXT): Bio of the user (fetched from Telegram)
- `coins` (INT): Number of coins the user has (virtual currency)
- `joined_date` (DATETIME): Timestamp when the user joined the bot
- `role` (ENUM): User role (`owner`, `developer`, `sudo`, 'enforcer', `user`)
- `is_scanned` (BOOLEAN): Indicates whether the user is scanned (true/false)
 
📗 **groups**
- `_id` (BIGINT): Unique ID of the Telegram group (Primary Key)
- `name` (VARCHAR): Name of the group
- `member_count` (INT): Number of members in the group
- `created_at` (DATETIME): Timestamp when the group was created
- `is_scanned` (BOOLEAN): Whether the group is scanned by the BlueAPI


📙📕
