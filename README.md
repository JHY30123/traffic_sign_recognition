# nvidia_traffic_sign

### Running container and start jupyter notebook
```bash
sudo docker run --runtime=nvidia -it \
-v /path/to/dir/on/host:/workspace/tlt-experiments \
-p 8888:8888 nvcr.io/nvidia/tlt-streamanalytics:v2.0_py3 /bin/bash


jupyter notebook --ip 0.0.0.0 --allow-root
```
