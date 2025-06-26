# Polyglot Environment Setup

## Quick Setup Commands

### 1. Update Your Existing f_sharp Environment
```powershell
# Update your existing f_sharp environment
conda env update -f environment.yml

# Activate your f_sharp environment
conda activate f_sharp

# Register Python kernel with Jupyter (using f_sharp env)
python -m ipykernel install --user --name=f_sharp --display-name "Python (f_sharp)" --force
```

### 2. Install .NET Interactive (for F# support)
```powershell
# Verify .NET SDK is installed
dotnet --version

# Install .NET Interactive tool globally
dotnet tool install -g Microsoft.dotnet-interactive

# Register .NET kernels with Jupyter
dotnet interactive jupyter install
```

### 3. VS Code Extensions Required
- **Polyglot Notebooks** (ms-dotnettools.dotnet-interactive-vscode)
- **Jupyter** (ms-toolsai.jupyter)

## Testing Your Setup

1. Open `notebooks/polyglot_test.dib`
2. Select kernels when prompted:
   - F# cells → `.NET Interactive F#`
   - Python cells → `Python (f_sharp)`
3. Execute both cells - should output identical mathematical results

## Troubleshooting

### F# Kernel Not Available
```powershell
# Reinstall .NET Interactive
dotnet tool uninstall -g Microsoft.dotnet-interactive
dotnet tool install -g Microsoft.dotnet-interactive
dotnet interactive jupyter install
```

### Python Kernel Issues
```powershell
# Recreate kernel registration for f_sharp environment
conda activate f_sharp
python -m ipykernel install --user --name=f_sharp --display-name "Python (f_sharp)" --force
```

### Environment Variables (if needed)
Add to your PATH:
- `%USERPROFILE%\.dotnet\tools` (for .NET tools)
- Your conda installation path

## Ready for Development!

Once both kernels work in `polyglot_test.dib`, you can:
- Create module-specific notebooks
- Use F# for symbolic/logical work
- Use Python for numerical analysis
- Combine both in the same notebook!
