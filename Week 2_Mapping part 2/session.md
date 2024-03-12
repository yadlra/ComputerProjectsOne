## Hour 1

Learning objectives: Discuss findings from fieldwork and challenges faced during data collection

What does it mean to standardise data?

A critical aspect of data standardisation in the context of data management and integration.

Why does it matter in computer science?

Data standardization is converting data into a standard format that computers can easily understand and use. For example, when you standardize data, you might convert all measurements into the metric system or all dates into a single format (such as YYYY-MM-DD).


    What types of data did we collect?

    Business Name: Holborn Cafe
    Postcode: WC1A 1AB
    Phone Number: 020 1234 5678
    Social Media: facebook.com/holborncafe
    Business Hours:
        Monday to Friday: 8 AM - 6 PM
        Saturday: 9 AM - 4 PM
        Sunday: Closed

Make a list of data types for our map

    Business Name: This is textual data and typically falls under the "string" data type. Standardizing it might involve ensuring consistent capitalization and formatting (e.g., always using "Holborn Cafe" instead of "holborn cafe" or "Holborn Café").
    Postcode: This is alphanumeric data and can be standardized by ensuring a consistent format, such as removing spaces and converting all letters to uppercase (e.g., WC1A1AB).
    Phone Number: This is numerical data but is usually treated as a string due to the presence of dashes or spaces. Standardizing it might involve removing special characters and ensuring a consistent format (e.g., 02012345678).
    Social Media: This is textual data and typically falls under the "string" data type. Standardizing it might involve ensuring consistent formatting (e.g., always using "facebook.com/holborncafe" instead of variations like "www.facebook.com/holborncafe").
    Business Hours: This data represents time intervals and days of the week. Standardizing it might involve converting the time to a 24-hour format for consistency (e.g., "8:00 AM - 6:00 PM" becomes "08:00 - 18:00"). Additionally, you could represent the days consistently, such as using "Mon" for Monday and "Sat" for Saturday.

    How can we abstract and standardise them?

e.g. numbers, text, formatted text like post codes, specific types of establishments.

Abstracting and standardizing data involves defining a common structure and format for the information you collect. This process ensures consistency and facilitates easy processing and analysis. Here's how you can abstract and standardize the data provided for "Holborn Cafe":

Task: Make a list of places, add data for each data type we identified.

    What’s missing?
    Do we need more information?

## Hr 2

We will do this section together

Standardisation using Python Pandas library


    * Open your vscode IDE
    * Create file

We need to have Pandas installed

pip install pandas

https://github.com/yadlra/foundation-comp-project-one

Task: Use OpenStreetMap query API to search our map

    Try at least one of the exercises on this page https://wiki.openstreetmap.org/wiki/OSMPythonTools

    You can follow the code in file osm_exercise.ipynb in github 

    https://github.com/yadlra/foundation-comp-project-one

Task: Finalise your journal from week 1

