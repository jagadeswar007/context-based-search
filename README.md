This repository contains the code and infra setup required for the Context based search and below is the simple architecture as of now.
# Architecture
<img width="849" height="158" alt="image" src="https://github.com/user-attachments/assets/97e90ebd-7c77-43b1-a71f-9458647ffd0c" />

# Problem statement:
Normal text search can be done easily using the Mongodb if the user know what they need to search, the problem comes when the user don’t have the exact text to search only know what is the over all context that require.

## Tech Stack:
1. MongoDB
2. LLM for vector embedding
3. React Js
4. Python
5. AWS Services
   1. S3
   2. API Gateway
   3. Lambda functions

# Solution:
The possible solution is to enable the sematic search which is available in the Mongo Atlas version 8 and above. This approach is effective as it returns with the data to the user which is nearest match for his search if there is no exact match for the search.
## Implementation: 
The tech stack which is being used is React for the hosting simple web page which has some search box for taking user input and this can be hosted on the s3 bucket using s3 static web site hosting.
Used one of the LLM for converting the text into the Vectors and stored them in the Mongodb along with the text in the json format. In the mongodb created the vector index for the key which hold the vector embeddings. The code required for this conversion is written using Python language.
While searching the data the same LLM model has to be used to convert the text into vector for more accurate results and form the query aggregation and search the data accordingly.
To achieve this we have created a API gateway integrated with lambda function. Lambda function has two functions one is to convert the data into the vectors and inserting that  into the mongodb. The other is to query the data from the mongodb for the context based search.



