
# Creating an environment from an environment.yml file

1. Create the environment from the ```environment.yml``` file
  - **Linux CPU only**
```sh
$ conda env create -f dl_env_linux.yml
```
   - **Linux With GPU support**
```sh
$ conda env create -f dl_env_linux_gpu.yml
```

2. Activate the new environment:

- Windows: ```activate myenv```
- macOS and Linux: ```source activate myenv```
NOTE: Replace myenv with the name of the environment.
Verify that the new environment was installed correctly:

conda list
