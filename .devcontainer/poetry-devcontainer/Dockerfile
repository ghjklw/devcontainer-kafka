ARG VARIANT="3.11-bullseye"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=vscode

RUN DEBIAN_FRONTEND=noninteractive \
    && apt update \
    && apt install -y build-essential --no-install-recommends wget curl bash-completion iputils-ping


ENV HOME="/home/$USER"
ENV PATH="$PATH:${HOME}/.local/bin"

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.in-project true
RUN chown -R $USER: $HOME/.config/pypoetry
