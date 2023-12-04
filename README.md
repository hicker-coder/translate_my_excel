# Infomineo Document Translator

Infomineo Translator is a Python application built with Streamlit that allows users to upload various types of documents, including PDFs, Word documents, and Excel files. It provides the functionality to translate text within these documents to a selected destination language. For Excel files, it translates the content of individual cells while keeping the original columns intact.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Uploading Documents](#uploading-documents)
  - [Translating Text](#translating-text)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7 or higher installed on your system.
- The required Python packages installed. You can install them using pip:


### Installation

1. Clone the repository to your local machine:

## Usage

### Running the Application

To run the tool Translator, use the following command in your terminal while in the project directory:
This command starts a local server, and the application can be accessed through your web browser at `http://localhost:8501`.

### Uploading Documents
1. Once the application is running, you can upload documents by clicking the "Upload a PDF, Word, or Excel document" button.
2. Select a document from your local file system.

### Translating Text

#### PDF and Word Documents

1. After uploading a PDF or Word document, select your desired destination language from the dropdown menu.
2. Click the "Translate" button.
3. The translated text will be displayed in the app, and you can download it as a text file.

#### Excel Files

1. After uploading an Excel file, select your desired destination language from the dropdown menu.
2. Click the "Translate" button.
3. The translated Excel file with original columns intact will be available for download as an Excel file.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the project.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



