# Hospital Bed Management System

A comprehensive desktop application built with Python and tkinter for efficient hospital bed management, patient tracking, and predictive analytics. The system provides real-time bed availability monitoring, patient admission tracking, and statistical analysis tools for hospital administrators and medical staff.

## 🌟 Key Features

### 👥 User Roles & Access Control
- **Administrators**
  - System configuration and monitoring
  - Bed management and allocation
  - Statistical analysis and reporting
  - User activity audit logs
- **Doctors**
  - Patient admission management
  - Bed transfer handling
  - Discharge processing
  - Patient history access

### 💻 Core Functionality
- **Secure Authentication**
  - Role-based access control
  - Encrypted password storage
  - Session management

- **Patient Management**
  - New patient registration
  - Medical history tracking
  - Admission status monitoring
  - Discharge processing

- **Bed Management**
  - Real-time bed status tracking
  - Multiple bed categories
  - Maintenance scheduling
  - Occupancy monitoring

- **Analytics & Reporting**
  - Average Length of Stay (ALOS) calculation
  - Predictive discharge date estimation
  - Bed occupancy trends
  - Interactive statistical graphs
  - CSV export functionality

### 📊 Dashboard Features

#### 👨‍⚕️ Doctor Dashboard
- Quick patient search and filtering
- Bed availability view
- Patient admission processing
- Transfer management interface
- Discharge handling

#### 👨‍💼 Admin Dashboard
- **Analytics**
  - Interactive statistical graphs
  - ALOS trends
  - Bed utilization metrics
  
- **Management**
  - Bed inventory control
  - User activity monitoring
  - System configuration

## 🚀 Getting Started

### Prerequisites
- Python 3.11+ (3.11.9 recommended)
- MySQL Server 8.0+
- Windows OS (tested on Windows 10/11)

### Required Python Packages
- ttkbootstrap >= 1.17.0
- Pillow >= 11.3.0
- matplotlib >= 3.8.0
- mysql-connector-python >= 8.2.0
- mypy >= 1.7.0 (for development)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nicku2/hospital-bed-management-system.git
   cd hospital-bed-management-system
   ```

2. **Set Up Virtual Environment** (Recommended)
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   - Create a MySQL database
   - Update database credentials in `database/connection.py`
   - Run database initialization:
     ```bash
     python database/init_db.py
     ```

5. **Start the Application**
   ```bash
   python main.py
   ```
   Or use the provided `start.bat` file.

## 🎯 Usage Guide

### First-Time Setup
1. Launch the application
2. Log in with default admin credentials:
   - Username: admin
   - Password: admin123
3. Change the default password
4. Set up additional user accounts as needed

### Regular Usage
1. **For Doctors**
   - Log in with doctor credentials
   - View assigned patients
   - Process admissions/discharges
   - Manage bed transfers

2. **For Administrators**
   - Monitor bed utilization
   - Review statistics and reports
   - Manage system settings
   - Export data as needed

## 📝 Project Structure
```
hospital-bed-system/
├── analytics/         # Analytics and calculations
├── auth/             # Authentication and user management
├── database/         # Database connections and schemas
├── graphs/          # Generated statistical graphs
├── ui/              # User interface components
├── utils/           # Utility functions
├── main.py          # Application entry point
└── requirements.txt  # Python dependencies
```

## 🔒 Security Features
- Encrypted password storage
- Role-based access control
- Session management
- Audit logging of all actions
- Input validation and sanitization

## 📈 Future Enhancements
- Mobile application integration
- Real-time notifications
- AI-powered bed allocation
- Integration with hospital EHR systems
- Advanced analytics dashboard

## 🤝 Contributing
Contributions are welcome! Please feel free to submit pull requests.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors
- nick23r (Project Lead)

## 🙏 Acknowledgments
- TTK Bootstrap for the modern UI components
- Python community for excellent libraries
- Contributors and testers

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
