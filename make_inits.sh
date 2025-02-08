#!/bin/bash

TARGET_PATH="gen/python"

if [ ! -d "$TARGET_PATH" ]; then
  echo "Error: $TARGET_PATH is not a directory."
  exit 1
fi

find "$TARGET_PATH" -type d -exec touch "{}/__init__.py" \;

echo "__init__.py files created in all directories under $TARGET_PATH"
