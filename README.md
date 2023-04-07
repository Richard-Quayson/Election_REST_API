# Ashesi Voting System API

This project creates APIs for an election voting system. The API provides **functionalities**
that allow a client to:
1. Register a voter -> POST. 
2. De-register a voter -> PATCH.
3. Update a voter's information -> PUT.
4. Retrieve a voter's information (behaves as a filter system) -> GET.
5. Create an election -> POST.
6. Retrieve an election's details -> GET.
7. Delete an election -> DELETE.
8. Vote in an election -> POST.


## v1 (version 1)
The first version of the API uses the [flask framework](https://flask.palletsprojects.com/en/2.2.x/) to create an app that provides
the functionaities listed above. It uses a .txt file as the database.

### Usage 
**Note:** If a folder with name data, does not exist, create in the v1 folder and create empty .txt
files named voters.txt and elections.txt.
```
**Folder name:** data
**Voters filename:** voters.txt
**Elections filename:** elections.txt
```

You can check tests performed on the API in the test_result.pdf file in v1.


## v2 (version 2)
The second version of the API uses the [flask framework](https://flask.palletsprojects.com/en/2.2.x/) to create an app that provides
the functionaities listed above. It uses a firebase database for storing information.

### Usage 
**Note:** Create a firebase database and update the key.json file with the database credentials.
```
**Filename to be updated:** key.json
```


## v3 (version 3)
The third version of the API uses the functions framework to create an http function that routes request to functions that define
the functionaities listed above. It uses a firebase database for storing information.

### Usage 
**Note:** Create a firebase database and update the key.json file with the database credentials.
```
**Filename to be updated:** key.json
```

The function has been deployed to google cloud and can be tested using any HTTP client like [Postman](https://www.postman.com/)
at this [address](https://us-central1-rest-api-lab-5.cloudfunctions.net/ashesi_election_api/)

You can check tests performed on the API in the test_result.pdf and test_result_updated.pdf files in v3.


## General (for v1 and v2)
To run the program, set up a virtual environment and install the packages in the requirements.txt
file. Activate the virtual environment, move into the version's directory (i.e. v1 or v2) in your terminal and run the 
voting_system.py file. You can test the API functionalities using any HTTP client like [Postman](https://www.postman.com/)

```Python

# run the voting_system.py file
python voting_system.py
```


## Program Overview:
For an overview on the project, check the file task_instructions.pdf in v1, v2, and v3.


## Future updates:
The project defined helper functions that performed uniqeueness tests for data. It also defines some amount of validation
tests for voter information. However, it assumes validation of request data for creating an election. As such, future updates will:
- [ ] Implement validation for election data.
- [ ] Improve validation of voter's information.
- [ ] Provide endpoints for managing (creating, updating, deleting, and retrieving) an election's positions and candidates.
- [ ] Improve runtime filter for retrieving voter information (e.g. student_id, email, should have higher priorities since they are unique).
- [ ] Possibly create a frontend and integrate with this API (😶‍🌫️🧐🤯).


## Message:
****It's Richard here, happy coding 😁😂✌️💪❗****
