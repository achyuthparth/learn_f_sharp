# Multi-stage Dockerfile for F# + Python Polyglot Notebooks Environment
# Base: Ubuntu with .NET SDK and Anaconda for polyglot development

FROM mcr.microsoft.com/dotnet/sdk:9.0 AS base

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH
ENV DOTNET_ROOT=/usr/share/dotnet
ENV PATH=$PATH:$DOTNET_ROOT:$DOTNET_ROOT/tools

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    git \
    vim \
    curl \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh && \
    conda clean -a -y

# Create non-root user
RUN useradd -m -s /bin/bash developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER developer
WORKDIR /home/developer

# Copy environment configuration
COPY --chown=developer:developer environment.yml .

# Create conda environment from YAML
RUN conda env create -f environment.yml && \
    conda clean -a -y

# Activate environment and register Python kernel
RUN /bin/bash -c "source $CONDA_DIR/etc/profile.d/conda.sh && \
    conda activate f_sharp && \
    python -m ipykernel install --user --name=f_sharp --display-name 'Python (f_sharp)'"

# Install .NET Interactive tools
RUN dotnet tool install -g Microsoft.dotnet-interactive

# Add dotnet tools to PATH for the user
ENV PATH="/home/developer/.dotnet/tools:$PATH"

# Register .NET Interactive kernels with Jupyter
RUN /bin/bash -c "source $CONDA_DIR/etc/profile.d/conda.sh && \
    conda activate f_sharp && \
    export JUPYTER_PATH=$CONDA_DIR/envs/f_sharp/share/jupyter && \
    dotnet-interactive jupyter install"

# Copy project files
COPY --chown=developer:developer . /home/developer/learn_f_sharp/

# Set working directory to project
WORKDIR /home/developer/learn_f_sharp

# Create startup script
RUN echo '#!/bin/bash' > start.sh && \
    echo 'source $CONDA_DIR/etc/profile.d/conda.sh' >> start.sh && \
    echo 'conda activate f_sharp' >> start.sh && \
    echo 'export PATH="/home/developer/.dotnet/tools:$PATH"' >> start.sh && \
    echo 'echo "🚀 F# + Python Polyglot Environment Ready!"' >> start.sh && \
    echo 'echo "📁 Project files in: /home/developer/learn_f_sharp"' >> start.sh && \
    echo 'echo "🧪 Test notebook: notebooks/polyglot_test.dib"' >> start.sh && \
    echo 'echo ""' >> start.sh && \
    echo 'echo "Available commands:"' >> start.sh && \
    echo 'echo "  jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root"' >> start.sh && \
    echo 'echo "  dotnet --version"' >> start.sh && \
    echo 'echo "  python --version"' >> start.sh && \
    echo 'echo "  conda list"' >> start.sh && \
    echo 'echo ""' >> start.sh && \
    echo '/bin/bash' >> start.sh && \
    chmod +x start.sh

# Expose Jupyter port
EXPOSE 8888

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD /bin/bash -c "source $CONDA_DIR/etc/profile.d/conda.sh && conda activate f_sharp && python -c 'import sys; print(sys.version)' && dotnet --version"

# Default command
CMD ["./start.sh"]

# Build instructions (add to README):
# docker build -t fsharp-polyglot .
# docker run -it -p 8888:8888 -v $(pwd):/home/developer/learn_f_sharp fsharp-polyglot

# For Jupyter Lab access:
# docker run -it -p 8888:8888 fsharp-polyglot jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
