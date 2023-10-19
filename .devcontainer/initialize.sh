#!/bin/bash
set -x

# Convenience workspace directory for later use
WORKSPACE_DIR=$(pwd)

if [ ! -f ~/.initialized ]; then
    # git config
    git config --local core.editor 'code --wait'

    # Change some Poetry settings to better deal with working in a container
    poetry config cache-dir "${WORKSPACE_DIR}/.cache"

    # Enable poetry auto-completion
    poetry completions bash >> ~/.bash_completion

    touch ~/.initialized
fi

# Now install all dependencies
poetry install --with dev

# Install pre-commit
poetry run pre-commit install --install-hooks
