---

# Tableau Server Bulk Users Roles Update Script

## Overview

This Python script automates the process of updating BULK users roles on a Tableau Server based on data from a CSV file. It connects to the Tableau Server, checks the current roles of specified users, and updates them if necessary. After making changes, it logs the updates and exports a report detailing the restored access to an Excel file.

## Features

- **Automated Role Update:** The script reads user roles from a CSV file and updates them on the Tableau Server as needed.
- **Detailed Logging:** Logs details of all role changes, including users whose roles were not updated.
- **Report Generation:** Generates an Excel report listing all users, their previous roles, and their updated roles (if changed).
- **Integration with Tableau Server Client Library:** Utilizes the `tableauserverclient` library to interact with Tableau Server.

## Prerequisites

1. **Python 3.x**: Ensure Python 3.x is installed on your machine.
2. **Required Python Libraries**: Install the following libraries:
   - `pandas`: For handling data and exporting to Excel.
   - `tableauserverclient`: For interacting with Tableau Server.
   
   You can install the required libraries using pip:
   ```bash
   pip install pandas tableauserverclient
   ```

3. **Configuration File**: The script relies on a `config` file containing the following variables:
   - `server`: The URL of your Tableau Server.
   - `user_name`: The username to authenticate with Tableau Server.
   - `password`: The password associated with the username.

4. **Input File**: Ensure you have a CSV file named `users_roles_update.csv` with the following columns:
   - `site`: The site ID where the user belongs.
   - `username`: The username whose role needs to be updated.
   - `role`: The new role to assign to the user.

## Script Description

1. **Initialization**:
   - The script starts by connecting to the Tableau Server using the credentials provided in the `config` file.
   - It then reads the CSV file `users_roles_update.csv` which contains the user details and the roles to be updated.

2. **Role Update Process**:
   - For each user, the script checks if their current role matches the role specified in the CSV file.
   - If the roles do not match, the script updates the user's role on Tableau Server and logs the change.
   - If the roles match, it logs that no update was required.

3. **Report Generation**:
   - The script appends details of each update (or lack thereof) to a DataFrame.
   - Once all users are processed, it exports the DataFrame to an Excel file named with the current timestamp (e.g., `26-08-2024 15-30-00-Restored Access.xlsx`).
   - The report is saved in the `data-files` directory.

4. **Completion**:
   - The script prints the DataFrame to the console and confirms that all users have been updated.

## Usage

1. **Set Up the Configuration**:
   - Ensure the `config` file is correctly set up with your Tableau Server details.

2. **Prepare the Input CSV File**:
   - Prepare the `users_roles_update.csv` file with the correct format as mentioned above.

3. **Run the Script**:
   - Execute the script in your Python environment:
   ```bash
   python main.py
   ```

4. **Check the Output**:
   - Review the console output to see a summary of the updates.
   - Open the generated Excel report in the `data-files` directory for detailed information.

## Output Example

```
Connecting to Tableau Server: https://tableau.yourserver.com
WillSmith role changed to: Explorer
BruceLee role not changed to: Viewer
...
```

## Conclusion

This script provides a streamlined solution for managing user roles on Tableau Server, ensuring that roles are updated efficiently and accurately. With detailed logging and report generation, it offers both transparency and accountability in the role management process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
