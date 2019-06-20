# World Of Games

### How to:

**Build**: 
- ```docker-compose build```

**Run**:
- ```docker-compose up -d```

**Play the g**ame**:
- ```docker exec -it wog python main_game.py```

**Run test**:
- ```docker exec -it wog python tests/e2e.py```
- Should return 0 if test pass and -1 if not

**Clean**:
- ```docker-compose down;docker rmi $(docker images -q)```

**Run Jenkins test**:
- Set the following environment variables:
    - DOCKER_ID
    - DOCKER_PASSWORD

- Build Pipeline script from SCM


**Links**:
- [Game](http://localhost:8777)
- [Selenium](http://localhost:4444/grid/console)