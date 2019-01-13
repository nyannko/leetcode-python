#!/usr/bin/env bash
# bash-boilerplate from
# https://github.com/alphabetum/bash-boilerplate/blob/master/bash-simple
# first create the clean gh-page branch
# https://gist.github.com/ramnathv/2227408
# cd /path/to/repo-name
# git symbolic-ref HEAD refs/heads/gh-pages
# m .git/index
# git clean -fdx
# and then run this script under the gitbook directory
# example: bash gitbook_script.sh leetcode leetcode-python

set -u

_simple() {
	gitbook_dir=$1
	github_repo=$2
	cat >gbsync.sh <<EOF
gitbook build
cd \$HOME/github/${github_repo}/
git co gh-pages 
cp -r \$HOME/github/gitbooks/${gitbook_dir}/_book/* \$HOME/github/${github_repo}/
git add .
dt=\$(date '+%d/%m/%Y,%H:%M')
git commit -m \$dt
git push -u origin gh-pages
git co master
EOF
}

_ME=$(basename "${0}")

_print_help() {
	cat <<HEREDOC
Usage:
  ${_ME} [gitbook_dir] [github_repo]
  ${_ME} -h | --help
Options:
  -h --help  Show this screen.
HEREDOC
}

_main() {
	# Avoid complex option parsing when only one program option is expected.
	if [[ "${1:-}" =~ ^-h|--help$ ]]; then
		_print_help
	else
		_simple "$@"
	fi
}

# Call `_main` after everything has been defined.
_main "$@"
