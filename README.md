# AutoClean

According config file,  gzip file or remove file.

## Configuration

```yaml
autoclean:
  schedule: "* * * * *"
  paths:
    - dirctory: "/data/logs"  # absolute path
      filename: "*.log"       # filename (eg test.log *.log)
      command: gzip           # command (only gzip or remove)
      expire: 15              # expire days
```  

## Run

```
git clone https://github.com/wooos/autoclean.git
cd autoclean

pip3 install -r requirements.txt
python autoclean.py [CONFIG]
```

## Run with docker

Create `autoclean.yaml` config file.

```
autoclean:
  paths:
    - directory: /data/logs
      filename: *.log
      command: gzip
      expire: 7
    - directory: /data/logs
      filename: *.gz
      command: rm
      expire: 15
```

Run autoclean.

```
docker run -d -v autoclean.yaml:/etc/autoclean/autoclean.yaml -v /data/logs:/data/logs wooos/autoclean
```

