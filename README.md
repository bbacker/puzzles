
docker build -t perm_letters:latest .

docker run --rm -it perm_letters:latest -s ripece | sort | tee out.txt
