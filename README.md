# Hospital Bed Management System

A comprehensive desktop application for managing hospital beds, patient admissions, and bed transfers with predictive analytics.

## Features

### User Roles
- **Admin**: System configuration, audit log monitoring, bed management, analytics
- **Doctor**: Patient admissions, bed transfers, discharge management

### Core Features
1. **Dual-Level Authentication**: Secure login system with role-based access
2. **Patient Management**: Admit patients, manage medical history, track admissions
3. **Bed Management**: Add beds, track bed status (available/occupied/maintenance)
4. **Bed Transfers**: Transfer patients between beds with reason tracking
5. **Search & Filter**:
   - Doctors: Search by patient name, bed ID, admission reason
   - Admins: Filter audit logs by user and date range
6. **ALOS Analytics**: Calculate Average Length of Stay and predict discharge dates
7. **Audit Logging**: Track all system actions for compliance
8. **CSV Export**: Export audit logs, admissions, beds, and statistics

### Dashboard Features

#### Doctor Dashboard
- View active admissions
- Search and filter patients
- Admit new patients
- Discharge patients
- Transfer patients to different beds
- Real-time bed availability

#### Admin Dashboard
- **Audit Logs Tab**: View and filter system actions by user and date
- **Bed Management Tab**: Add new beds, view all beds and their status
- **Statistics Tab**: View system statistics and ALOS data

## Installation

### Prerequisites
- Python 3.8+
- MySQL Server

### Setup

1. **Install dependencies**:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

2. **Initialize database**:
\`\`\`bash
python -c "from database.init_db import initialize_database; initialize_database()"
\`\`\`

3. **Run the application**:
\`\`\`bash
python main.py
\`\`\`

## Database Schema

### Tables
- **users**: Admin and doctor accounts
- **beds**: Hospital bed inventory
- **patients**: Patient information
- **admissions**: Patient admission records
- **bed_transfers**: Bed transfer history
- **audit_logs**: System action audit trail
- **alos_statistics**: Average length of stay statistics

## Demo Credentials

- **Admin**: username: `admin_user`, password: `admin123`
- **Doctor**: username: `dr_smith`, password: `doctor123`

## File Structure

\`\`\`
hospital-bed-system/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── database/
│   ├── schema.sql         # Database schema
│   ├── connection.py      # Database connection manager
│   └── init_db.py         # Database initialization
├── auth/
│   └── authentication.py  # Authentication and audit logging
├── ui/
│   ├── login_window.py    # Login interface
│   ├── doctor_dashboard.py # Doctor interface
│   └── admin_dashboard.py  # Admin interface
├── analytics/
│   └── alos_calculator.py # ALOS calculations and predictions
└── utils/
    └── csv_export.py      # CSV export functionality
\`\`\`

## Usage

### Doctor Workflow
1. Login with doctor credentials
2. View active admissions
3. Use search/filter to find specific patients
4. Admit new patients (fills bed automatically)
5. Transfer patients between beds
6. Discharge patients when ready

### Admin Workflow
1. Login with admin credentials
2. View audit logs with filtering options
3. Add new beds to the system
4. Monitor system statistics and ALOS data
5. Export reports to CSV

## Features in Detail

### Search & Filter
- **Doctor Dashboard**: Real-time filtering by patient name, bed ID, or admission reason
- **Admin Dashboard**: Filter audit logs by user and date range

### CSV Export
- Export audit logs with timestamp
- Export admissions data
- Export bed inventory
- Export ALOS statistics
- Export bed transfer history

### ALOS Analytics
- Automatic calculation of average length of stay by bed type
- Discharge date predictions based on historical data
- Occupancy rate calculations
- Admission trend analysis

## Security Features
- Password hashing with SHA-256
- Role-based access control
- Comprehensive audit logging
- User action tracking

## Theme
The application uses the **Superhero** theme from ttkbootstrap for a modern, professional appearance.

## Support

For issues or questions, please refer to the database logs or check the console output for error messages.
