#!/usr/bin/env bash

# The following comments should help you get started:
# - Bash is flexible. You may use functions or write a "raw" script.
#
# - Complex code can be made easier to read by breaking it up
#   into functions, however this is sometimes overkill in bash.
#
# - You can find links about good style and other resources
#   for Bash in './README.md'. It came with this exercise.
#
#   Example:
#   # other functions here
#   # ...
#   # ...
#
#   main () {
#     # your main function code here
#   }
#
#   # call main with all of the positional arguments
#   main "$@"
#
# *** PLEASE REMOVE THESE COMMENTS BEFORE SUBMITTING YOUR SOLUTION ***

main() {
  declare -A colors=( [black]=0 [brown]=1 [red]=2 [orange]=3 [yellow]=4 [green]=5 [blue]=6 [violet]=7 [grey]=8 [white]=9 )
  [[ -z "${colors[$1]}" || -z "${colors[$2]}" ]] && echo "invalid color" && exit 1

  echo "${colors[$1]}${colors[$2]}"
}

main "$@"