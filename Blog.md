# EcoSanity: Promoting Cleanliness with AI

## Introduction
Public spaces often struggle with issues of cleanliness and hygiene due to activities like littering and improper disposal of waste. Despite efforts to raise awareness, these problems persist, affecting community well-being and the environment. **EcoSanity** aims to address this by using AI-powered video surveillance to detect and alert about littering activities in real-time. With an intelligent system like EcoSanity, we strive to make public spaces cleaner and more sanitary, promoting a culture of responsibility and cleanliness in our communities.

## The Idea Behind EcoSanity
The inspiration for EcoSanity arose from observing the ongoing littering problems in parks, streets, and other public areas. We noticed that while campaigns and regulations exist to discourage littering, enforcement is often limited due to the lack of effective monitoring. Our goal was to leverage AI and modern technology to create a tool that could monitor such activities, provide immediate feedback, and generate reports to help authorities take action. By utilizing real-time surveillance, we wanted to create a system that not only detects and alerts but also educates and promotes cleaner habits within communities.

## Project Overview
EcoSanity is an AI-powered application designed to identify and report littering activities in real-time. Users can upload videos or stream live feeds to monitor public spaces. The system analyzes the footage for specific activities, such as human littering or pet urination, and provides voice-over alerts when incidents are detected. Additionally, EcoSanity generates summary reports that include timestamps of the detected activities. This detailed analysis assists community members and authorities in maintaining cleaner environments and promoting responsible behavior.

## Technology Stack
The development of EcoSanity involved the integration of several technologies:
- **Python**: The primary programming language used for implementing application logic.
- **OpenCV**: For video processing and analysis to detect specific activities in both uploaded videos and live streams.
- **Streamlit**: To build an intuitive front-end interface that allows users to upload videos, analyze streams, and access summary reports.
- **OpenAI**: To generate voice-over alerts in real-time when specific activities are detected.
- **NVIDIA Workbench**: Used to leverage GPU acceleration, ensuring efficient processing of high-resolution videos.
- **FFmpeg**: For handling video encoding, decoding, and processing within the application.
- **AlmaLinux**: As the server operating system on our Namecheap server, providing a stable and secure environment for deployment.

## How EcoSanity Was Built
EcoSanity was built using Python as the core language, leveraging OpenCV for video processing and activity detection. The application starts by allowing users to upload video files or stream live feeds through a user-friendly interface built with Streamlit. Once a video is uploaded or a live stream is provided, OpenCV processes the frames to identify specific activities, such as littering or pet urination.

When an incident is detected, the application utilizes the OpenAI API to generate an immediate voice-over alert, informing the user of the activity. For instance, if a littering event is identified, a message like "Littering detected at [timestamp]" is generated and played through the system.

To ensure performance and real-time processing, we hosted the application on NVIDIA Workbench, taking advantage of GPU acceleration. This setup was crucial for handling large video files and high-definition live streams, providing faster and more accurate detection results. In addition to real-time alerts, we implemented a summary report feature. By clicking the "Generate Summary Report" button, the application compiles all detected activities into a comprehensive report, including timestamps, providing valuable data for community review and action.

Finally, we integrated the application with Streamlit's interface to offer an accessible front end for non-technical users. This interface provides simple controls for uploading videos, analyzing streams, and viewing detailed reports, making EcoSanity a versatile tool for various settings.

## Challenges and Solutions
One of the major challenges was ensuring the accuracy of activity detection in diverse environments, such as varying lighting conditions and video qualities. We addressed this by fine-tuning our AI model with a variety of training data to minimize false positives. Integrating OpenAI for real-time voice generation also required optimizing the processing pipeline to maintain the application's responsiveness. By using NVIDIA’s Workbench and GPU acceleration, we were able to enhance performance, enabling near real-time analysis even for high-definition videos.

## Conclusion and Future Work
EcoSanity successfully demonstrates the potential of AI in promoting sanitation and cleanliness in public spaces. By providing real-time alerts and detailed reports, it encourages responsible behavior and aids authorities in maintaining a cleaner environment. Moving forward, we plan to expand EcoSanity’s detection capabilities, introducing more nuanced activity recognition. Additionally, we aim to develop a mobile-friendly version of the app, making it even more accessible for community use and monitoring.

## Learn More
For a detailed explanation, visit the [GitHub Repository](https://github.com/sureshora/hackathon5dellnividia.git).
Try Live Project: Visit the [myportfolio] (https://sureshwizard.com/project4)
