# GIT - распределенная система контроля версий
# Это система для отслеживания и ведения истории изменения файлов, в вашем проекте. При помощи распределенности git еще и организовывается командная работа.


# Репозиторий - это хранилище вашего кода и истории его изменений

#------#------#------#------#------#------#------#------#------#------

# GitHub - веб сайт дя размещения git-репозиториев в совместной разработке проектов

#------#------#------#------#------#------#------#------#------#------
# Команды GIT:
# 1. git init -> она создает локальный гит репозиторий у вас на ПК, в той директории в которой была прописана команда.

# 2. git status -> команда для проверки статуса наших файлов

# 3. git add -> команда для добавления файлов в систему отслеживания гита, после этой команды изменения начинают фиксироваться

# 4. git commit -m 'comment' -> команда для сохранения версии в локальном репозиотории, вместе с комментарием к изменениям

# 5. git remote add origin <url> -> это команда для того чтобы установить связь локального репозитория с удаленным в гитхабе

# 6. git push -> команда для отправки ваших изменений в локальном репо в удаленный репо
         #git push origin main


# 1*) git init
#         2) git add .
#         3) git commit -m ''
# 4*) git remote add origin <url>
#         5) git push origin main


##------##------##------##------##------##------##------##------##------##------##------



# These are common Git commands used in various situations:

# start a working area (see also: git help tutorial)
#    clone     Clone a repository into a new directory
#    init      Create an empty Git repository or reinitialize an existing one

# work on the current change (see also: git help everyday)
#    add       Add file contents to the index
#    mv        Move or rename a file, a directory, or a symlink
#    restore   Restore working tree files
#    rm        Remove files from the working tree and from the index

# examine the history and state (see also: git help revisions)
#    bisect    Use binary search to find the commit that introduced a bug
#    diff      Show changes between commits, commit and working tree, etc
#    grep      Print lines matching a pattern
#    log       Show commit logs
#    show      Show various types of objects
#    status    Show the working tree status

# grow, mark and tweak your common history
#    branch    List, create, or delete branches
#    commit    Record changes to the repository
#    merge     Join two or more development histories together
#    rebase    Reapply commits on top of another base tip
#    reset     Reset current HEAD to the specified state
#    switch    Switch branches
#    tag       Create, list, delete or verify a tag object signed with GPG

# collaborate (see also: git help workflows)
#    fetch     Download objects and refs from another repository
#    pull      Fetch from and integrate with another repository or a local branch
#    push      Update remote refs along with associated objects

##------##------##------##------##------##------##------##------##------##------##------

# 1) git init
# 2) git add .
# 3) git commit -m "comment"
# 4) git remote git@add копируйте и вставляете при создании нового репозитория
# 5) git branch -M main
# 6) git push origin main

                        # после каждого изменения
# 1) git Add
# 2) git commit -m "comment"
# 3) git push origin main

# git branch -> все ветки
# git branch <название> создание новой ветки
# git checkout <название ветки> переход на ветку
# git branch -D <название ветки> удаление ветки

# git merge <название другой ветки> слияние текущей ветки с названной веткой

# git clone <ссылка на репозиторий> клонирование или скачивание данного репозитория

# git push origin main отправка изменения
# git pull стягивание изменений