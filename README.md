**Reddit Data Engineering Project**

This project showcases my proficiency in data engineering, orchestrating the extraction, analysis, 
and storage of Reddit data seamlessly through Docker containers and Apache Airflow.

**Key Features:**

1. **Containerized Workflow Management**: Docker containers streamline the entire data pipeline. The setup includes:

   - Airflow Worker: Executes data processing tasks efficiently in parallel.
   - Airflow Webserver: Provides a user-friendly interface for workflow monitoring and management.
   - Task Scheduler: Coordinates task execution based on predefined schedules, ensuring pipeline integrity.
   - PostgreSQL Database: Serves as a reliable storage solution for metadata and task tracking.

2. **Task 1: Reddit Data Extraction and Sentiment Analysis**:

   - **Reddit Data Extraction**: Python scripts integrated into the Airflow workflow use the PRAW library to extract data from specified subreddits.

   - **Sentiment Analysis with NLTK and Nrclex**: Sentiment analysis is performed on Reddit post content using Natural Language Toolkit (NLTK) and Nrclex libraries. This analysis enhances data comprehension by evaluating the emotional tone of the text.

   - **Data Cleaning and Transformation**: Meticulous data cleaning and transformation operations ensure data quality and consistency post-sentiment analysis. The cleaned data is formatted and prepared for further analysis.

   - **Export to CSV**: Processed data is exported to CSV format for compatibility with various analytical tools and platforms.

3. **Task 2: Data Upload to Datalake (S3 Bucket)**:

   - **Automated Data Upload**: The project automates the upload of processed Reddit data to a datalake, specifically an S3 bucket. This cloud-based storage solution ensures data availability and accessibility for downstream analytics and processing.

**Skills Demonstrated:**

- Docker Containerization for Workflow Isolation and Scalability
- Apache Airflow Workflow Management for Task Orchestration
- PRAW Library for Reddit Data Extraction
- NLTK and Nrclex for Sentiment Analysis
- PostgreSQL Database for Metadata Storage
- Data Cleaning and Transformation Techniques
- Data Export to CSV
- Data Upload to AWS S3 Datalake
