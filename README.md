# Nvidia Traffic Sign Recognition

## 1. Environment Describition
### Training 
|               | Version         |
|---------------|-----------------|
| OS            | Ubuntu 18.04    |
| Nvidia Driver | 440             |
| CUDA Version  | CUDA 10.02-base |

### Inference
|          | Version          |
|----------|------------------|
| OS       | Ubuntu 18.04 L4T |
| CUDA     | 10.2             |
| CUDNN    | 8.0.0            |
| TensorRT | 7.1.0            |

## 2. Running
### Creating container and starting jupyter notebook
```bash
sudo docker run --runtime=nvidia -it \
-v /path/to/dir/on/host:/workspace/tlt-experiments \
-p 8888:8888 nvcr.io/nvidia/tlt-streamanalytics:v2.0_py3 /bin/bash

jupyter notebook --ip 0.0.0.0 --allow-root
```

### Entering the container created before
```bash
sudo docker ps -l  # Get the latest ran containerID

sudo docker start containerID

sudo exec -it containerID /bin/bash
```
The program could be trained after converting label format and path setting up. `inference.ipynb` is used on deploying pretrained model on Jetson platform.
