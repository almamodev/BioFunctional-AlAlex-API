# BioFunctional AlAlex API Documentation

## Overview

The BioFunctional AlAlex API is a Flask-based web service designed to interact with the KEGG (Kyoto Encyclopedia of Genes and Genomes) database. It provides functionalities to upload files, process pathway information, and update data based on pathway interactions.

## Installation

To set up the KEGG API, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

    ```
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```
    python app.py
    ```

## Usage

### Uploading Files

You can upload files to the KEGG API using a POST request to the `/kegg` endpoint. The file should be provided as part of the request payload.

### Processing Pathways

Once a file is uploaded, the API processes the pathway information contained within the file. It extracts interactions, reactions, and relations from the KEGG database.

### Updating Data

The API updates the uploaded file based on the pathway information obtained. It identifies relevant data in the file and modifies it to include pathway interactions and reactions.

### Error Handling

The API handles various error scenarios, such as missing columns in the uploaded file and request exceptions during pathway processing.

## Dependencies

The KEGG API relies on the following Python packages:

- Flask: A lightweight web framework for building web applications.
- Flask-Smorest: An extension for Flask that adds support for OpenAPI documentation.
- Beautiful Soup: A Python library for parsing HTML and XML documents.
- Requests: A HTTP library for making requests in Python.
- Marshmallow: A library for object serialization and validation.

## Contributors

- [Albert Martín Moreno]
- [Alejandro Rodriguez Mena]
- [Antonio Monleon Getino]

## License

This project is licensed under the [MIT License](LICENSE).
