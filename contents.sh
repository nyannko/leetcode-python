#!/usr/bin/env bash
# automatically generate contents with its md file 
set -u

# gitbook dir
HOME_DIR="$HOME/github/gitbooks/leetcode/"
# original title
title="$@"
name=$(echo $title | sed -e 's/\. /_/g' -e 's/ /_/g')
# generated title
FILE="${name}.md"

# touch new md file if not exists
if [[ ! -e "$HOME_DIR/alg/${FILE}" ]]; then
	echo "### ${title}" >${HOME_DIR}/alg/${FILE}
else
	echo "file already exists.."
fi

content="\t* [${title}](alg/${FILE})"
# create new contents.. todo: compare equality of ${content} with -1 line
echo -e "${content}" >> $HOME_DIR/SUMMARY.md # escape * with double quotes
