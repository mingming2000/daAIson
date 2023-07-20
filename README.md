# daAIson!

## How to commit
```
$ git add <file-or-folder-name>
$ git commit -m "<message for this commit>"
```

## How to create/use branch
```
$ git branch <name> # create a new branch
$ git checkout <name> # move to the target branch
# examples
$ git branch advanced # 'advanced' is the name of the new branch
$ git checkout advanced # move to 'advanced' branch
```

## How to merge branch
```
$ git checkout <base-branch-name>
$ git merge <target-branch-name>
```
- `base-branch-name`: 기본 브랜치 (뼈대가 되는 브랜치).
- `target-branch-name`: 합치기 원하는 브랜치(branch).

## How to push to github
```
$ git push origin main
# or
$ git push origin <branch-name>
```

## How to pull github repo into local desktop/laptop
```
$ git pull origin main
# or
$ git pull origin <branch-name>
```
- 만약 레포(repo)가 없는 컴퓨터에 다운받고 싶다면, 아래 명령어를 사용하시오.
```
$ git clone https://github.com/mingming2000/daAIson.git
```