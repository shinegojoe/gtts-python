you need to install the dependency manual after the CI/CD
ex: if pip install translate in the develop environment
go to the deploy server, into the container
ex: sudo docker exec -ti gtts /bin/bash
pip install translate and pm2 restart gtts 