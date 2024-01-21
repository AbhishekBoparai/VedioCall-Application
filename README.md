# VedioCall-Application
ConnectHub - Video Conferencing App
ConnectHub is a comprehensive video conferencing application developed with Django, HTML, CSS, JavaScript, and powered by Zegocloud. This repository contains the source code for ConnectHub, offering users a feature-rich platform for seamless meeting creation, joining, in-app chat, and screen sharing.

Features
User Authentication: Secure user registration and login functionality for a personalized experience.
Meeting Creation and Joining: Users can effortlessly create new virtual meetings or join existing ones.
In-App Chat: Real-time communication during meetings with a built-in chat feature.
Screen Sharing: Enhance collaboration by sharing screens, presentations, or documents directly.
Technologies Used
Django: A high-level Python web framework for backend development.
HTML, CSS, JavaScript: Frontend technologies for building a responsive and interactive user interface.
Zegocloud: Utilized for a reliable infrastructure supporting video conferencing.
Getting Started
Follow these steps to set up and run ConnectHub locally on your machine.

Prerequisites
Python (3.7 or higher)
Django (3.0 or higher)
Zegocloud API Key (Sign up on Zegocloud to obtain your API key)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/ConnectHub.git
Navigate to the project directory:

bash
Copy code
cd ConnectHub
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure Zegocloud API Key:

Obtain your Zegocloud API key from Zegocloud.
Set the API key in the ConnectHub settings.
Apply migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Access ConnectHub in your browser at http://localhost:8000/.

Configuration
Configure the following settings in the settings.py file:

ZEGOCLOUD_API_KEY: Set your Zegocloud API key here.
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance ConnectHub.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to Zegocloud for providing a reliable video conferencing infrastructure.
The Django community for creating a powerful web framework.
Experience seamless video conferencing with ConnectHub! 🚀
