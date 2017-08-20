
# How to Setup a Python Environment for Machine Learning and Deep Learning with Anaconda

## 1. Download the Anaconda Python package for your platform 

1. Visit the [Anaconda homepage](https://www.continuum.io/).
2. Click “Anaconda” from the menu and click “Download” to go to the [download page](https://www.continuum.io/downloads).
![](http://3qeqpr26caki16dnhd19sv6by6v.wpengine.netdna-cdn.com/wp-content/uploads/2017/02/Click-Anaconda-and-Download.png)

3. Choose the download suitable for your platform (Windows, OSX, or Linux):
- Choose Python 3.6
- Choose the Graphical Installer(Windows, OSX)

![](https://i.imgur.com/4zkN7XG.png)

This will download the Anaconda Python package to your workstation.

## 2. Detailed Anaconda installation information
This step assumes you have sufficient administrative privileges to install software on your system.
For installation instructions, see the following:

- **Installing on Windows** (https://docs.continuum.io/anaconda/install/windows)
- **Installing on macOS** (https://docs.continuum.io/anaconda/install/mac-os)
- **Installing on Linux** (https://docs.continuum.io/anaconda/install/linux)

## 3. Creating an environment from an environment.yml file

In this step, we will install Python libraries used for deep learning, specifically: Theano, TensorFlow, and Keras, nltk.
Most of machine learning and deep learning libraries needed are provided in the ```yaml (.yml)``` files.

1. Create the environment from the ```environment.yml``` file
  - **Linux CPU only**
```sh
$ conda env create -f dl_env_linux.yml
```
   - **Linux With GPU support**
```sh
$ conda env create -f dl_env_linux_gpu.yml
```

 - **Windows CPU only**
```sh
$ conda env create -f dl_env_windows.yml
```

- **macOS CPU only**
```sh
$ conda env create -f dl_env_mac.yml
```

2. Activate the new environment:

- Windows: ```activate myenv```
- macOS and Linux: ```source activate myenv```

NOTE: Replace myenv with the name of the environment. 

3. Verify that the new environment was installed correctly:

```sh
$ conda list
```
