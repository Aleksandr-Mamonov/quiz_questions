# Quiz questions API
## Requirements:
* docker >= 24
* docker-compose

## Quick Start
1. Clone this repository:  
```
git clone https://github.com/Aleksandr-Mamonov/quiz_questions.git
```
2. Change directory:  
```
cd quiz_questions
```
4. Create and configure your own `.env` file with following environment variables:
    - `DATABASE_USERNAME`
    - `DATABASE_PASSWORD`
    - `DATABASE_NAME`
5. Run docker-compose:  
```
docker-compose up -d
```
7. After all containers are up and running, try out API:  
    - using curl:  
    ```
    curl -H "Content-Type: application/json" -X POST -d '{"questions_num":1}' http://0.0.0.0:8000/quiz/api/v1.0/save_quiz_questions
    ```  
    - or navigate to [http://localhost:8000/docs](http://localhost:8000/docs) in your browser and try it via interactive docs

To stop docker-compose run 
```
docker-compose down
```
