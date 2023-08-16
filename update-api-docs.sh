#!/bin/bash

python3 -m pip install lazydocs

mkdir -p docs

python3 -m pip install .
lazydocs --overview-file index.md .
rm ./docs/.pages

# Echo to overwrite pre-commit's exit code
echo "Done!"
