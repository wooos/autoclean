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
python autoclean.py [CONFIG]
```