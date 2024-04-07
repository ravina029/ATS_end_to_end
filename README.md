# ATS web application. 
# Building an Application Tracking System (ATS) with Gemini-Pro API and streamlit application

Gemini-Pro provides a powerful API that enables developers to build custom solutions for various tasks, including application tracking systems (ATS). In this guide, we'll walk through the steps to build an ATS using the Gemini-Pro API.


steps to run the app
1. clone the repository "https://github.com/ravina029/ATS_end_to_end/tree/main"
2. install the dependencies in the requirements.txt file using the command "pip install -r requirements.txt"
3. generate the GOOGLE_API_KEY from makersuite ans save in .env file 
4. run the command "streamlit run App.py"

Note: This application doesn't give the best accuracy due to following reasons.

1. Large Language Models (LLMs) like Gemini Pro are inherently stochastic, meaning they introduce a random element in their generation process. This can lead to slight variations in the output even with the same input.
2. To mitigate this, you can run the system multiple times and consider the average score or the most frequent suggestions across runs.
