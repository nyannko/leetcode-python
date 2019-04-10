set -e
gitbook build
cd $HOME/github/leetcode-python/
git co gh-pages 
cp -r $HOME/github/gitbooks/leetcode/_book/* $HOME/github/leetcode-python/
git add .
dt=$(date '+%d/%m/%Y,%H:%M')
git commit -m ${dt}
# comsg=$@
# echo ${comsg}
# if [[ $# -eq 0 ]]; then # if no commit msg
#     git commit -m ${dt}
# else 
#     git commit -m ${comsg}
# fi
git push -u origin gh-pages
git co master
