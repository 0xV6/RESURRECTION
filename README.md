# RESURRECTION - A BLOOD DONATION PLATFORM

[![GitHub issues](https://img.shields.io/github/issues/zeroxv6/RESURRECTION)](https://github.com/zeroxv6/RESURRECTION/issues)
[![GitHub forks](https://img.shields.io/github/forks/zeroxv6/RESURRECTION)](https://github.com/zeroxv6/RESURRECTION/network)
[![GitHub stars](https://img.shields.io/github/stars/zeroxv6/RESURRECTION)](https://github.com/zeroxv6/RESURRECTION/stargazers)
[![GitHub license](https://img.shields.io/github/license/zeroxv6/RESURRECTION?style=for-the-badge&label=License&color=blue)](https://opensource.org/licenses/GPL-3.0)




## Overview

RESURRECTION is a cutting-edge project that aims to revolutionize the blood donation process. This project attempts to streamline blood donation by providing real-time donation requests, monitoring contribution histories, and an interactive map to help donors find nearby hospitals.

## Features
 
1. **Dual Posting System (Users & Hospitals)**  
   Both **individual users** and **hospitals** can post blood requirements, ensuring quicker communication and better accessibility for donors.  

2. **Urgency-Based Requests**  
   Requests can be categorized by urgency levels (**Critical, High, Moderate**) to help prioritize donations and notify potential donors immediately.  

3. **Easy Donor Registration**  
   Donors can **proactively sign up** to indicate their willingness to donate blood, allowing them to be contacted even when no specific request is posted.  

4. **Nearby Hospitals on Interactive Map**  
   A **dedicated Maps section** helps users locate nearby hospitals and blood banks, ensuring quick and easy access to donation centers.  

5. **Appointments & Scheduling**  
   Users can **view, book, and manage blood donation appointments** directly from the platform, ensuring a hassle-free donation experience.  

6. **Donation History & Records**  
   A **personalized history section** allows users to track their past donations, see upcoming appointments, and maintain a record of their contribution to saving lives.  

These features create a smooth and efficient blood donation system, making it easier for donors and recipients to connect while ensuring timely and life-saving interventions. 🚑💉

## Installation

To get started with RESURRECTION, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/zeroxv6/RESURRECTION.git
    ```
2. Navigate to the project directory:
    ```sh
    cd RESURRECTION
    ```
You can add the provided SQL setup code under the "Setup Database" section in your README like this:


## Setup Database

To set up the database for **RESURRECTION Blood Donation**, follow these steps:

1. **Create the Database**:
   ```sql
   CREATE DATABASE resurrection_blood_donation;
   USE resurrection_blood_donation;
   ```

2. **Create User Registration Table**:
   ```sql
   CREATE TABLE users (
                           id INT AUTO_INCREMENT PRIMARY KEY,
                           full_name VARCHAR(100) NOT NULL,
                           phone_number VARCHAR(15) NOT NULL UNIQUE,
                           email VARCHAR(100) NOT NULL UNIQUE,
                           address TEXT NOT NULL,
                           blood_type VARCHAR(3) NOT NULL,
                           created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. **Create Hospital Registration Table**:
   ```sql
   CREATE TABLE hospitals (
                               id INT AUTO_INCREMENT PRIMARY KEY,
                               hospital_name VARCHAR(200) NOT NULL,
                               hospital_address TEXT NOT NULL,
                               hospital_phone VARCHAR(15) NOT NULL UNIQUE,
                               hospital_email VARCHAR(100) NOT NULL UNIQUE,
                               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

4. **Create Blood Donation Posts Table**:
   ```sql
   CREATE TABLE blood_posts (
                                 id INT AUTO_INCREMENT PRIMARY KEY,
                                 name VARCHAR(100) NOT NULL,
                                 phone VARCHAR(15) NOT NULL,
                                 address TEXT NOT NULL,
                                 blood_type VARCHAR(3) NOT NULL,
                                 urgency ENUM('normal', 'urgent', 'critical') DEFAULT 'normal',
                                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

5. **Create Donation Offers Table**:
   ```sql
   CREATE TABLE donation_offers (
                                     id INT AUTO_INCREMENT PRIMARY KEY,
                                     blood_type VARCHAR(3) NOT NULL,
                                     last_donation_date DATE,
                                     medical_conditions TEXT,
                                     availability VARCHAR(100),
                                     contact VARCHAR(15) NOT NULL,
                                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

6. **Insert Sample Blood Donation Posts**:
   ```sql
   INSERT INTO blood_posts (name, phone, address, blood_type, urgency, created_at) VALUES
   ('Name', '111-111-1111', '123 Park Street, Sector 17, Chandigarh', 'A+', 'urgent', '2025-01-19 16:30:00'),

   ```

7. **Create Appointments Table**:
   ```sql
   CREATE TABLE appointments (
                                  id INT AUTO_INCREMENT PRIMARY KEY,
                                  user_id INT NOT NULL,
                                  hospital_id INT NOT NULL,
                                  appointment_date DATE NOT NULL,
                                  appointment_time TIME NOT NULL,
                                  notes TEXT,
                                  status ENUM('scheduled', 'completed', 'cancelled') DEFAULT 'scheduled',
                                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                  FOREIGN KEY (user_id) REFERENCES users(id),
                                  FOREIGN KEY (hospital_id) REFERENCES hospitals(id)
   );
   ```

8. **Create Donation History Table**:
   ```sql
   CREATE TABLE donation_history (
                                      id INT AUTO_INCREMENT PRIMARY KEY,
                                      user_id INT NOT NULL,
                                      hospital_id INT NOT NULL,
                                      blood_type VARCHAR(3) NOT NULL,
                                      donation_date DATE NOT NULL,
                                      status ENUM('completed', 'cancelled') NOT NULL,
                                      notes TEXT,
                                      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                      FOREIGN KEY (user_id) REFERENCES users(id),
                                      FOREIGN KEY (hospital_id) REFERENCES hospitals(id)
   );
   ```

This SQL setup will create the necessary tables and insert some initial data into the **blood_posts** table to test the database and website connectivity. Adjust the data as needed for your application.


## Contributing

We welcome contributions from the community. To contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## Meet the Developers

### Deepanshu Sharma

- [GitHub](https://github.com/DeepanshuSharma05)
- [X.com](https://x.com/i_deepanshu05)

### Raman Mann

- [GitHub](https://github.com/zeroxv6)
- [X.com](https://x.com/raman_205)

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Tech Stack

- HTML,CSS,Tailwind,JavaScript,Python(Flask Server),MySQL


---

