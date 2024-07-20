# Hospitality Room Allocation

This web application helps in digitalizing the hospitality process for group accommodation. Users can upload CSV files with group and hostel information, and the application will allocate rooms accordingly.

## Features

- Upload group and hostel information via CSV files.
- Allocate rooms ensuring the same group ID stays together.
- Separate accommodations for boys and girls.
- Ensure room capacities are not exceeded.
- Display and download room allocation results.

## How to Run

1. Clone the repository:
   git clone <repository_url>
   cd hospitality_app

2. python3 -m venv venv
   .\venv\Scripts\activate      #for windows to activate the virtual env
   source venv/bin/activate     #for mac os to activate the virtual env
   pip install -r requirements.txt

3. Python main.py
   
4. http://127.0.0.1.5000   


## Breif Explanation of the Logic

### Detailed Logic

1. File Upload:
   - The user uploads two CSV files: one for group information and one for hostel information.
   - The application reads and parses these files to extract the necessary data.

2. Data Processing:
   - The group information CSV contains fields for Group ID, Members, and Gender.
   - The hostel information CSV contains fields for Hostel Name, Room Number, Capacity, and Gender.

3. Allocation Algorithm:
   - Group Segregation: Groups are segregated based on their gender to ensure boys and girls are allocated to their respective hostels.
   - Room Assignment:
     - Iterate through each group and attempt to allocate them to available rooms in the respective hostel.
     - Check if the room has sufficient capacity to accommodate the entire group.
     - If a room cannot accommodate the entire group, the group is split across multiple rooms while ensuring that each member of the group is accommodated.
   - Update Room Capacity: After each allocation, the room's remaining capacity is updated.

4. Result Compilation:
   - The results are compiled into a structure that maps Group ID to Hostel Name, Room Number, and Members Allocated.

5. Output Display and Download:
   - The allocation results are displayed on the web interface.
   - Users can download the allocation details as a CSV file.

### Example Allocation Logic

1. Input Data:

   Group Information CSV:
   
   Group ID,Members,Gender
   101,3,Boys
   102,4,Girls
   103,2,Boys
   104,5,Girls
   105,8,Boys & Girls