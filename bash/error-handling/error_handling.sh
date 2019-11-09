#!/usr/bin/env bash

main () {

    (( $# != 1 )) && echo "Usage: ./error_handling <greetee>" && exit 1

    echo "Hello, ${1}"

}

main "$@"