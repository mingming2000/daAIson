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

## Running python on Ubuntu
> ([ref](https://austcoconut.tistory.com/entry/%EB%AC%B4%EC%9E%91%EC%A0%95-%EB%94%B0%EB%9D%BC-%ED%95%98%EA%B8%B0-LinuxUbuntu%EC%97%90%EC%84%9C-Python-%EA%B0%9C%EB%B0%9C-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95-python3-%EC%84%A4%EC%B9%98-pip-%EC%84%A4%EC%B9%98))
