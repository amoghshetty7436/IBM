
# NutriScan: AI-Driven Nutritional Deficiency Detection

## Overview

NutriScan is an innovative, AI-powered system designed to detect nutritional deficiencies by analyzing visual anomalies in the eyes, nails, and teeth. The system leverages advanced technologies, including IBM's Vision and Language Models, CNNs, MobileNetV2, and Watson Machine Learning, to provide accurate, real-time diagnostics. Along with identifying deficiencies, NutriScan generates personalized dietary recommendations and precautionary measures, empowering users to take proactive steps toward better health.

## Key Features

- **AI-Powered Multi-Modal Analysis:** Detects visual anomalies using IBM Vision Models, CNNs, and MobileNetV2 for accurate results.
- **Personalized Health Insights:** Provides customized dietary recommendations based on detected deficiencies using IBM's Large Language Models (LLMs).
- **Seamless Integration with IBM Cloud:** Cloud-based storage with IBM Cloudant and AI deployment through IBM Watson Machine Learning.
- **User-Friendly Web Interface:** Built with Django, offering easy navigation and interaction for users to check their health status and receive recommendations.
- **Scalable and Secure:** Cloud-based infrastructure ensures scalability and data security for healthcare professionals and individual users alike.

## Technologies Used

- **IBM Vision Model:** For detecting visual anomalies in eyes, nails, and teeth.
- **IBM Large Language Models (LLMs):** For classifying anomalies and generating personalized recommendations.
- **MobileNetV2:** Efficient deep learning architecture for image processing and anomaly detection.
- **Django (Python):** Framework for building the web interface.
- **IBM Cloudant:** NoSQL cloud database for secure data storage.
- **IBM Watson Machine Learning:** For deploying AI models and real-time inference.
- **Python Environment:** For executing the Python-based application.

## Installation & Setup

### Prerequisites:
- Python 3.x
- Django
- IBM Cloud and Watson account (for AI services and Cloudant)

### Steps to Run the Project:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd nutritional_diagnosis
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up IBM Cloud services (follow the documentation to set up IBM Vision, LLMs, and Watson Machine Learning).

4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

5. Access the application in your browser at `http://127.0.0.1:8000`.

## Usage

Once the server is running, users can interact with the web interface to upload images for analysis. The system will process the images, identify potential nutritional deficiencies, and provide personalized recommendations based on the detected anomalies.

## Future Scope

- **Expanded Visual Indicators:** Additional features like skin, tongue, and hair analysis.
- **Integration with Wearable Devices:** Real-time health monitoring and updates.
- **Global Health Recommendations:** Custom recommendations based on regional health trends.
- **Medical Collaborations:** Partnerships with hospitals for real-world deployment and validation.
- **Telemedicine Integration:** Remote consultations for broader accessibility.

## Contributing

Contributions are welcome! If you'd like to contribute to NutriScan, please fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License.

---

This README provides a detailed yet concise overview of your project while ensuring clarity for users on how to set up and run the system.
