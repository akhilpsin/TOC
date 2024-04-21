# Touch of Care (TOC) | hospital management|  Django Project  
  
## Overview  
  
Touch of Care (TOC) is an innovative web-based platform designed to streamline and enhance the hospital experience for patients, staff, and management. By centralizing hospital-patient data, the system reduces manual work, minimizes paperwork, and maintains up-to-date information accessible to administrators in real-time. TOC aims to provide a hassle-free, efficient, and digitally evolved healthcare environment, where administrative tasks are simplified, and patient care is the primary focus.  
  
## Objective  
  
The main objective of the Touch of Care project is to create a comprehensive digital solution for hospitals that simplifies the complexities of healthcare management. It focuses on centralizing data, decreasing manual labor, reducing paperwork, and providing a real-time information platform for patients and administrators. The system also facilitates charitable contributions and supports medical emergencies, ensuring that healthcare services are accessible and efficient for all stakeholders.  
  
## Technical Details  
  
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Django Framework)  
- **Database:** SQLite3  
  
## Key Features  
  
- **User Portals:** Separate login portals for patients, doctors, and other hospital staff, each tailored to their specific needs and functions within the hospital.  
- **QR Code Integration:** Upon registration, patients receive a unique QR code, which is used to access a variety of hospital facilities and services.  
- **Patient Portal:** Features include health status monitoring, medicine schedules, historical medical data, and lab report access.  
- **Doctor Portal:** Doctors can access patient databases using the patient's QR code to insert prescriptions, notes, and lab test requests.  
- **Laboratory & Pharmacy Coordination:** Lab reports are uploaded directly to the patient's database, and prescribed medicines are organized in advance by the pharmacy, both identified through the patient's QR code.  
- **Admin Oversight:** Admins have full control over access permissions and can manage patient databases, ensuring smooth hospital operations.  
  
## Repository  
  
Access the source code for the Touch of Care project on GitHub:  
[TOC GitHub Repository](https://github.com/akhilpsin/TOC.git)  
  
For environment setup, please follow the instructions outlined in the `requirements.txt` file.  
  
## Quick Start  
  
Follow these steps to get the Touch of Care application up and running on your local environment:  
  
1. Clone the repository and navigate to the project directory:
   ```bash  
   git clone https://github.com/akhilpsin/TOC.git  
   cd TOC
   ```
2. Create and activate a virtual environment:
   ```bash
    py -m venv venv
    .\venv\Scripts\activate  # For Windows  
    source venv/bin/activate  # For Unix/MacOS
   ```
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```
4. Launch the Django server:
   ```bash
    python manage.py runserver
   ```
5. Visit http://127.0.0.1:8000/ in your browser to explore the application.
