# How to use Miniconda/Anaconda
This markdown file offers a quick guide to how to use Miniconda/Anaconda for beginners. 
If you have questions about Miniconda/Anaconda, feel free to contact me (HeumWoo Park, 010-2398-8643).
> **NOTE** You must delete my phone number before opening this repository to the Public! It is a sensitive part!

## What is Miniconda/Anaconda?
`Anaconda` is a distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment ([ref](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))).
The important point is `Anaconda` offers a distributed virtual environment that does not overlap/conflict with other environments.
Thus, you can easily manage or control your codes/projects without having to consider other environments or packagees.

`Minicoda` is a free minimal installer for `Anaconda`. It just installs a minimal enssential packages for your environment.

## Why is it important?
`Python` has multiple versions (3.5, 3.6, and later). 
However, users often want to use the specific version of packages or version of python.
If too many or various versions of packages or python are installed the same machine, the codes may be faced packages or python version conflicts.

To address this problem, a distributed virtual environment may be a good solution to avoid these conflicts.
This is because Miniconda/Anaconda offers a simple and strong distributed virtual environment without packages or python version conflicts.

## Then, how to use it?
> **NOTE** You need to understand that this Markdown is a quick guide on how to use Miniconda/Anaconda for begineers. No details are provided, so you may need to search for them in more detail via `Google`.
1. Create a new virtual environment
    ```
    $ conda create -n <env-name>                    # Essential!
    $ conda create -n <env-name> python=<version>   # [Optional] you can specify python version
    ```
2. Move in conda environment
    ```
    $ conda activate <env-name>
    ```
3. Move out conda environment
    ```
    $ conda deactivate
    ```
    - You do not need to declare an environment name.


# How to run Miniconda3 on Ubuntu (Edited by mkjeon)

> **NOTE** Run Ubunto terminal

## How to handle install Error 0x8007019e
Try [this](https://www.zinnunkebi.com/windows10-ubuntu-install-error/)

 
## Basic Ubuntu commends
1.
    ```
    $ vim test.py                                    # Open a file to be edited
    ```
2.    
    ```
    i                                                # Change to edit mode
    ```
3.    
    ```
    [Esc]                                            # Chage mode
    :wq                                              # Close the file
    ```
4.    
    ```
    $ python3 (file_name).py                            # Run python file
    ```

5. 
   ```
   mkdir (dir name)
   mkdir -p (dir name/file name)
    ```

6.  
    ```
    rmdir (dir name)
    ``` 
      
7. 
   ```
   touch (file name)
   cat > (file name)
   vi (file name)
   ```


8. 
    ```
    rm -rf (file name)
    ```

9. 
    ```
    mv [옵션] [이동시킬 디렉토리/파일] [이동 될 위치]

    ex) mv log.txt folder
    // 현재 디렉토리의 log.txt 파일을 folder 디렉토리로 이동

    ex) mv log.txt log2.txt
    // 현재 디렉토리의 log.txt 파일의 이름을 log2.txt로 변경

    ex) mv /app/bin/logs/log.txt /app/dw
    // /app/bin/logs 디렉토리의 log.txt 파일을 /app/dw 디렉토리로 이동
    ```


([Other commends](https://austcoconut.tistory.com/entry/%EB%AC%B4%EC%9E%91%EC%A0%95-%EB%94%B0%EB%9D%BC-%ED%95%98%EA%B8%B0-LinuxUbuntu%EC%97%90%EC%84%9C-Python-%EA%B0%9C%EB%B0%9C-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95-python3-%EC%84%A4%EC%B9%98-pip-%EC%84%A4%EC%B9%98))
     
## Activate Ctrl + V
Try [This](https://lungfish.tistory.com/entry/Ubuntu-%EC%9C%88%EB%8F%84%EC%9A%B0%EC%97%90%EC%84%9C-%EC%9A%B0%EB%B6%84%ED%88%AC-%EB%A6%AC%EB%88%85%EC%8A%A4%EB%A1%9C-%EB%B3%B5%EC%82%AC-%EB%B6%99%EC%97%AC-%EB%84%A3%EA%B8%B0%EA%B0%80-%EC%95%88%EB%90%A0-%EB%95%8C#:~:text=%E2%80%BB%20%EC%9C%88%EB%8F%84%EC%9A%B0%EC%97%90%EC%84%9C%20%EB%B3%B5%EC%82%AC%ED%95%A0,%2B%20Shift%20%2B%20V%20%EB%88%8C%EB%9F%AC%EC%95%BC%20%ED%95%A9%EB%8B%88%EB%8B%A4.)


## Install Miniconda3 on Linux (If you installed Miniconda3 'on Window')
1.
    ```
    $ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    ```
2.    
    ```
    $ bash Miniconda3-latest-Linux-x86_64.sh
    ```
3.    
    ```
    $ source ~/.bashrc
    ```
Now you can create virtual environment. ([ref](https://codingboycc.tistory.com/74))
    
If you can't excute virtual env, Try this. ([ref](https://technical-support.tistory.com/112))

    
    $ source (dir of linux)/miniconda3/etc/profile.d/conda.sh
    

