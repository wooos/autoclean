# AutoClean

According config file,  gzip file or rm file.

## Configuration

```yaml
autoclean:
  paths:
    - dirctory: "/data/logs"  # absolute path
      filename: "*.log"       # filename (eg test.log *.log)
      command: gzip           # command (only gzip or rm)
      expire: 15              # exrire days
```  

## Run

```
python autoclean.py [CONFIG]
```