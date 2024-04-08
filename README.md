# Application Tracking System using Gemini Pro

By [<b>Hema Kalyan Murapaka</b>](https://hemakalyan.netlify.app)

Connect with me on social media and explore my work:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/hemakalyan/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/KalyanMurapaka45)
[![Medium](https://img.shields.io/badge/Medium-Follow-03a57a?style=flat-square&logo=medium)](https://medium.com/@kalyanmurapaka274)
[![Twitter](https://img.shields.io/twitter/follow/KalyanM45?style=social)](https://twitter.com/KalyanM45)
[![Sponsor Hema Kalyan Murapaka](https://img.shields.io/badge/Sponsor-Hema_Kalyan-28a745?style=flat-square&logo=github-sponsors)](https://github.com/sponsors/KalyanMurapaka45)

**Special Thanks to GitHub Sponsors**

## About The Project

![](https://github.com/KalyanM45/Application-Tracking-System/blob/main/Artifacts/screen.png)
<br>
![](https://github.com/KalyanM45/Application-Tracking-System/blob/main/Artifacts/result.png)

The Smart Applicant Tracking System (ATS) is a cutting-edge tool designed to enhance the resume evaluation process. Leveraging advanced Generative AI models from Google, the system empowers users to submit their resumes for a comprehensive analysis based on a provided job description. The system, equipped with a keen understanding of the tech industry, including software engineering, data science, and big data engineering, evaluates resumes in the highly competitive job market. Users can upload their resumes in PDF format, and the system extracts relevant information using PyPDF2. The generated response includes a percentage match with the job description, a list of missing keywords, and a refined profile summary. This innovative solution aims to assist individuals in improving their resumes for optimal performance in the competitive job landscape. The Streamlit web application provides a user-friendly interface, making the resume enhancement process efficient and accessible.

## Built With

- Streamlit
- PyPDF2
- Google Generativeai
- Python-dotenv

## Getting Started

This will help you understand how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation Steps

### Option 1: Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**

   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
     ```
     git clone https://github.com/KalyanMurapaka45/Application-Tracking-System.git
     ```

2. **Create a Virtual Environment** (Optional but recommended)

   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)

   - Activate the virtual environment based on your operating system:
     ```
     conda activate <Environment_Name>/
     ```

4. **Install Dependencies**

   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**

   - Start the project by running the appropriate command.
     ```
     streamlit run app.py
     ```

6. **Access the Project**
   - Open a web browser or the appropriate client to access the project.

## API Key Setup

To use this project, you need an API key from Google Gemini Large Language Model. Follow these steps to obtain and set up your API key:

1. **Get API Key:**

   - Visit the Provided Link [Click Here](https://makersuite.google.com/app/apikey).
   - Follow the instructions to create an account and obtain your API key.

2. **Set Up API Key:**

   - Create a file named `.env` in the project root.
   - Add your API key to the `.env` file:
     ```dotenv
     GOOGLE_API_KEY=your_api_key_here
     ```

   **Note:** Keep your API key confidential. Do not share it publicly or expose it in your code.<br>

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

• **Report bugs**: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.

• **Contribute code**: If you are a developer and want to contribute, follow the instructions below to get started!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

• **Suggestions**: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or improvements you would like to see!

#### Don't forget to give the project a star! Thanks again!

## License

This project is licensed under the [Open Source Initiative (OSI)](https://opensource.org/) approved GNU General Public License v3.0 License - see the [LICENSE.txt](LICENSE.txt) file for details.<br>

## Contact Details

Hema Kalyan Murapaka - [kalyanmurapaka274@gmail.com](kalyanmurapaka274@gmail.com)<br>

## Acknowledgements

We'd like to extend our gratitude to all individuals and organizations who have played a role in the development and success of this project. Your support, whether through contributions, inspiration, or encouragement, has been invaluable. Thank you for being a part of our journey.
