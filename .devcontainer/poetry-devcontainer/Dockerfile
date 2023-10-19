ARG VARIANT="3.11-bullseye"
FROM mcr.microsoft.com/devcontainers/python:1-3.11-${VARIANT}

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=vscode

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y build-essential --no-install-recommends wget curl bash-completion


# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.in-project true
