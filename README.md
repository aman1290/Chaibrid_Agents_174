

used custom logs to store logs in logs folder 


workflow of project 

1. write every code with logging for making debugging easy
2. update helperfunction(tasks/function  which are repeated )
3. first test in research_notebook then only implement the code in src
4. validate for any error any optimixzation that need to be done will be done in research follder the update in code




graph TD
    A[Data Preparation] --> B[Embedding & Indexing]
    B --> C[Query Processing]
    C --> D[Generation]
    D --> E[Evaluation]
    E --> F[Deployment]
    F --> G[Monitoring & Iteration]