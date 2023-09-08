# Live Record

## usage
```bash
docker build . -t live_record
docker run --rm -d --name live_record -v `pwd`/videos:/app/videos live_record
```