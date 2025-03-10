# Electricity Billing System

## Description
The Electricity Billing System is a web-based application designed to manage electricity billing operations efficiently. It allows users to calculate bills, generate invoices, and visualize power consumption trends using charts and data analytics.

## Features
- User authentication and role-based access control (Admin & User)
- Customer registration and management
- Electricity bill generation and invoice management
- Power consumption analysis using dynamic charts
- Payment status tracking
- Data analytics for power usage trends
- Responsive UI for seamless interaction

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Java, PHP
- **Database:** MySQL
- **Data Analytics & Charts:** Python (for power chart generation)

## Installation & Setup
### Prerequisites
- XAMPP/WAMP for PHP & MySQL
- Java Development Kit (JDK)
- Python (for data analytics and chart generation)

### Steps to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/manmohanqqq/ebilling.git
   ```
2. Set up the database:
   - Import `ebilling.sql` into MySQL.
   - Configure database credentials in `config.php`.
3. Start the backend:
   - Run the Java server using `javac Server.java` followed by `java Server`.
4. Start the frontend:
   - Open `index.html` in a browser.
5. Generate analytics:
   - Run `python generate_charts.py` to update power consumption data.

## Usage
- **Admin Panel:**
  - Manage users and customers
  - Generate and track bills
  - View power consumption insights
- **User Panel:**
  - View and pay electricity bills
  - Track power consumption history

## Future Enhancements
- AI-based consumption prediction
- Secure online payment gateway integration
- Mobile app support

## Contributing
Feel free to contribute by submitting pull requests. Make sure to follow best practices and comment on your code.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact
For any queries or support, contact:
- Email: support@ebilling.com
- GitHub Issues: https://github.com/your-repo/ebilling/issues

