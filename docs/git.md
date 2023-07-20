# How to ues Git/Github for beginners
This markdown file offers a quick guide to how to use Git/Github for beginners. 
If you have questions about Git/Github, feel free to contact me (HeumWoo Park, 010-2398-8643).
> **NOTE** You must delete my phone number before opening this repository to the Public! It is a sensitive part!

## What is Git/Github?
- `git` is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency ([ref](https://git-scm.com/)).
The important point is that `git` is a **distributed version control system** for handling your codes or projects.
- `github` is a web service and cloud-based service that helps developers store and manage your codes, as well as track and control changes to your code ([ref](https://kinsta.com/knowledgebase/what-is-github/)).
The important point is that `github` is **a web service** and can be looked as **a cloud-based repository**.

## Why is it important?
It is useful when you are coding or managing for some project ([ref](https://www.makingscience.com/blog/what-is-git-and-why-it-is-so-important-to-use-it-in-our-projects/)).
- Collaboration with other people.
- Version management/storage
- Previous Version Restoration

> **NOTE** If you are interested in working as a software engineering/scientist, I think Git/Github is an important and enssential part.

## Then, how to use it?
> **NOTE** You need to understand that this Markdown is a quick guide on how to use Git/Github for begineers. No details are provided, so you may need to search for them in more detail via `Google`.
1. Check current status
    ```
    $ git status
    On branch main
    Your branch is up to date with 'origin/main'.

    Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
            modified:   README.md

    no changes added to commit (use "git add" and/or "git commit -a")
    ```
    ```
    $ git status .
    On branch main
    Your branch is up to date with 'origin/main'.

    Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
            modified:   README.md

    no changes added to commit (use "git add" and/or "git commit -a")
    ```
    - 뒤에 `.`이 없는 경우, 모든 경로(path)에 대해 변경/삭제/생성된 파일이나 폴더에 대해 출력.
    - 뒤에 `.`이 있는 경우, 현재 경로에 대해서 변경/삭제/생성된 파일이나 폴더에 대해 출력.

2. Commit your code/folders
    ```
    $ git add                    # [Option 1] Select all codes or folders for this project folder
    $ git add .                  # [Option 2] Select all codes or folders in the current path
    $ git add <file-or-folders>  # [Option 3] Select only specific codes or folders
    $ git commit -m "message for this commit"
    ```
    - `add` 뒤에 `.`를 사용하면, 현재 경로의 모든 파일/폴더를 선택.
    - `add` 뒤에 아무것도 입력 안하면, 모든 경로의 모든 파일/폴더를 선택.
    - `add` 뒤에 특정 파일이나 폴더를 입력하면, 그 파일/폴더만 선택.
    - `commi -m` 명령어를 사용하여 선택된 파일/폴더를 커밋(commit).
        - commit 해야만 새로운 버전과 state가 저장된다.

3. Push and Pull (Please read [this site](https://velog.io/@msung99/push-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EA%B9%83%ED%94%8C%EB%A1%9C%EC%9A%B0-pull))
    - Push repo to Github
    ```
    $ git push origin <branch-name>
    ```
    > **NOTE** If you want to push your current repo to Github for sharing your codes, you must commit your code before pushing.
    - Pull repo into your local desktop/laptop
    ```
    $ git pull
    $ git fetch
    ```

4. Branch and Merge
    - Create a new branch
    ```
    $ git branch                # Print all of branches
    $ git branch <branch-name>  # Create a new branch
    ```
    - Move branch
    ```
    $ git checkout <branch-name>
    ```
    - Merge branch
    ```
    $ git checkout main
    $ git merge <target-branch-name>
    ```

5. Roll-back (Please read [this site](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Reset-%EB%AA%85%ED%99%95%ED%9E%88-%EC%95%8C%EA%B3%A0-%EA%B0%80%EA%B8%B0))
    ```
    $ git reset --soft [commit]
    $ git reset --hard [commit]
    ```