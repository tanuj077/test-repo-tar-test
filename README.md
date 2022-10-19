# test-repo
Kindly ignore this repo.

```mermaid
sequenceDiagram
  User ->> Service 1: GET cache size limit request 
  
  Service 1->>+MySQL Database: Get Cache size limits from db
  MySQL Database->>-Service 1: Cache size limits
  Service 1 ->>+ User : Cache size limits
```

```mermaid
sequenceDiagram
  User ->> Service 1: PATCH cache size limit request 
  
  Service 1->>+MySQL Database: Update Cache size limits in db
  MySQL Database->>-Service 1: Success/Failure
  Service 1 ->>+ User : Success/Failure
```
