FastAPI Examples

This is a collection of examples for FastAPI.

It has been developed for the purpose of learning.

The project has been developed using Python 3.12.13 and FastAPI.
## Setup

``` markdown
Note: This project is built with UV package manager, it's recommended to use it.   
You can find the installation instructions on: 
https://docs.astral.sh/uv/getting-started/installation/
```

1. Clone the repository
2. Install dependencies via terminal with:
```bash
uv sync
```
3. Run the application via terminal with: 
```bash
uvicorn src.main:app --port 8080
```
4. Access the application at `http://localhost:8000`

## Endpoints

# Root

`GET /`

Returns a list of available endpoints in the application.

Response:
- Available endpoints
  - `/health`: Health check
  - `/task1`:
    - GET /task1/look: Gets the data stored for a key
    - POST /task1/newentry: Adds a new entry to the dictionary
  - `/task2`:
    - GET /task2: Gets the total price of the items and taxes
  - `/task3`:
    - GET /task3: Joins letters from the words in the query parameter

------------------------------------------------------------

### Health Check

`GET /health`

Checks whether the API is running.

Response:
- status: ok
- message: EPAM tasks

------------------------------------------------------------

### Task 1: Dictionary

#### Add New Entry

`POST /task1/newentry`

Adds a new key-value pair to the dictionary.

Query parameters:
- key
  - Type: string
  - Required: yes
  - Description: The dictionary key to add.

- value
  - Type: string
  - Required: yes
  - Description: The value associated with the key.

Example request:  
`POST /task1/newentry?key=name&value=John`

Successful response:
- `{"message": "Added name -> John to dictionary"}`

Missing parameter response:
- message: no key or value provided

------------------------------------------------------------

Lookup Entry

`GET /task1/look`

Looks up a value in the dictionary by key.

Query parameters:
- key
  - Type: string
  - Required: yes
  - Description: The dictionary key to search for.

Example request:  
`GET /task1/look?key=name`

Successful response:
- `{"message": "John"}`

Response when the key does not exist:
- `{"message": "No entry for name"}`

------------------------------------------------------------

### Task 2: Total Price Calculator

`GET /task2`

Calculates the total price of selected items including tax.

Query parameters:
- items
  - Type: list of strings
  - Required: yes
  - Description: The item names to include in the total. This parameter can be repeated.

- tax
  - Type: float
  - Required: yes
  - Description: The tax rate to apply. For example, 0.2 means 20%.

Request body:
- costs
  - Type: object/dictionary
  - Required: yes
  - Description: A dictionary where each key is an item name and each value is the item cost.

Example request:  
`GET /task2?items=apple&items=banana&tax=0.2`

Example request body:
```json
{
    "socks": 5,
    "shoes": 60,
    "sweater": 30
}
```

Successful response:
- `{"Total": 18.0}`

Missing data response:
- `{"message": "Missing parameters"}`

------------------------------------------------------------

### Task 3: Join Word Letters

`GET /task3`

Creates a new string by taking one letter from each word.

The endpoint uses the index of each word to select a letter from that word:
- From the first word, it takes the letter at index 0.
- From the second word, it takes the letter at index 1.
- From the third word, it takes the letter at index 2.

Query parameters:
- q
  - Type: list of strings
  - Required: yes
  - Description: List of words. This parameter can be repeated in the query string.

Example request:
GET /task3?q=apple&q=banana&q=cherry

Explanation:
- apple at index 0 gives a
- banana at index 1 gives a
- cherry at index 2 gives e

Successful response:
- `{"message": "aae"}`