FROM mcr.microsoft.com/vscode/devcontainers/base:bullseye AS base
COPY library-scripts/*.sh /tmp/library-scripts/

# Syntax: ./python-debian.sh [Python Version] [Python intall path] [PIPX_HOME] [non-root user] [Update rc files flag] [install tools flag] [Use Oryx if available flag] [Optimize when building from source flag]
# NOTE: 3.6 is out of support
FROM base AS python3.6
RUN /bin/bash /tmp/library-scripts/python-debian.sh 3.6 /usr/local/python3.6 "" "" "false" "false"

FROM base AS python3.7
RUN /bin/bash /tmp/library-scripts/python-debian.sh 3.7 /usr/local/python3.7 "" "" "false" "false"

FROM base AS python3.8
RUN /bin/bash /tmp/library-scripts/python-debian.sh 3.8 /usr/local/python3.8 "" "false" "false"

FROM base AS python3.9
RUN /bin/bash /tmp/library-scripts/python-debian.sh 3.9 /usr/local/python3.9 "" "false" "false"

FROM base AS devcontainer
# The Pythons we install need to be ahead of system bin dirs on the PATH
# otherwise tox will use system Python. (In theory that would be OK, but being
# consistent is simpler.)
# Note that python-debian.sh below adds 3.10 to the PATH via bash and zsh
# configs, but people using other shells won't see those changes. Updating the
# PATH here makes them available regardless of shell.
ENV PATH=/usr/local/python3.10/bin:\
/usr/local/python3.9/bin:\
/usr/local/python3.8/bin:\
/usr/local/python3.7/bin:\
/usr/local/python3.6/bin:\
/usr/local/py-utils/bin:\
$PATH

# Use Python 3.10 as the default Python — install utilities, etc as well as just
# Python.
RUN /bin/bash /tmp/library-scripts/python-debian.sh 3.10 /usr/local/python3.10

COPY --from=python3.6 /usr/local/python3.6 /usr/local/python3.6
COPY --from=python3.7 /usr/local/python3.7 /usr/local/python3.7
COPY --from=python3.8 /usr/local/python3.8 /usr/local/python3.8
COPY --from=python3.9 /usr/local/python3.9 /usr/local/python3.9

ENV PIPX_HOME=/usr/local/py-utils
ENV PIPX_BIN_DIR=$PIPX_HOME/bin
RUN pipx install tox

RUN mkdir -p /home/vscode/.vscode-server/extensions /home/vscode/.cache \
    && chown -R vscode:vscode /home/vscode/.vscode-server /home/vscode/.cache
