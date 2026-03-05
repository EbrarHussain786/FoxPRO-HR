# FoxPRO-HR — Complete Software Specification

## 1) Purpose
FoxPRO-HR is a centralized web-based HRMS to automate employee records, attendance, leave, payroll, recruitment, performance, training, documents, scheduling, reporting, roles/permissions, notifications, and system settings.

## 2) Core Modules
1. Employee Management
2. Attendance Management
3. Leave Management
4. Payroll Management
5. Recruitment Management
6. Performance Management
7. Training & Development
8. Document Management
9. Shift & Scheduling Management
10. Reporting & Analytics
11. User Roles & Permission Management
12. Notification & Communication System
13. System Settings & Configuration

## 3) Module-wise Functional Scope
### Employee Management
- Employee profile creation and lifecycle state (Active/Resigned/Terminated)
- Personal info: Name, CNIC, Address, Phone, Email
- Employment info: Department, Designation, Joining Date
- Salary and emergency contact
- Employee documents: CNIC, contracts, certificates

### Attendance
- Check-in / Check-out
- Biometric/device integration points
- GPS/device fingerprint tracking
- Late and overtime computation
- Attendance reports

### Leave
- Leave types: annual, sick, casual
- Leave balances
- Request workflow + manager approval
- Leave history

### Payroll
- Salary structure
- Allowances (mobile/transport)
- Deductions, overtime, tax
- Payslip generation

### Recruitment
- Job posting
- Candidate applications and resume storage
- Interview scheduling
- Candidate evaluation and hiring decision

### Performance
- KPI tracking
- Manager reviews
- Self-assessment
- Performance reports

### Training & Development
- Training calendar
- Course management
- Enrollments and certifications

### Documents
- Contracts, certificates, policies
- Expiry tracking

### Shift & Scheduling
- Shift templates and assignment
- Roster calendar

### Reporting & Analytics
- Dashboard KPIs
- Filtered operational reports

### Roles & Permissions
- Super Admin, HR Manager, Manager, Employee
- Role-based menu and access control

### Notifications & Communication
- In-app notifications
- Leave, payroll and policy announcements

### System Settings
- Company profile
- Attendance and leave policies
- Payroll cycle and tax configurations

## 4) Core Database Entities
- Employee
- Department
- Designation
- Attendance
- Leave_Request
- Payroll
- Salary_Structure
- Recruitment
- Candidate
- Performance_Review
- Training
- User
- Role
- Permission
- Notification

## 5) Dashboards
### Admin Dashboard
- Total Employees
- Today Attendance
- Leave Requests
- Payroll Summary
- Notifications

### Employee Dashboard
- My Attendance
- Leave Balance
- Salary Payslips
- Announcements

## 6) UI/UX Requirements
- Responsive and mobile friendly
- Clean dashboard cards
- Role-based menu
- Fast loading experience
- Search and filters
- Real-time notification ready architecture
- Transitions and subtle animations

## 7) Extra Professional Features Added
- Audit logging recommendation
- Backup/restore strategy recommendation
- 2FA/security policy recommendation
- API-ready integration points for biometric devices and third-party channels
